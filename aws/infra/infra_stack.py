from aws_cdk import (
    SecretValue,
    Stack,
    aws_amplify_alpha as amplify,
    aws_codebuild as codebuild
)
from constructs import Construct


class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        amplify_app = amplify.App(self, "Nextjs",
                                  source_code_provider=amplify.GitHubSourceCodeProvider(
                                      owner="david-authentic",
                                      repository="next-cdk",
                                      oauth_token=SecretValue.secrets_manager(
                                          secret_id="arn:aws:secretsmanager:us-east-1:875073938755:secret:github-token-4059es"
                                      ),
                                  ),
                                  auto_branch_deletion=True,
                                  build_spec=codebuild.BuildSpec.from_object_to_yaml({
                                      "version": "1.0",
                                      "frontend": {
                                          "phases": {
                                              "preBuild": {
                                                  "commands": ["npm ci"]
                                              }
                                          },
                                          "build": {
                                              "commands": ["env-cmd -f .env.${BUILD_ENV} npm run build"]
                                          },
                                      },
                                      "artifacts": {
                                          "baseDirectory": "out",
                                          "files": "/*"
                                      },
                                      "cache": {
                                          "paths": [
                                              "node_modules//*"
                                          ]
                                      }
                                  })
                                  )

        main = amplify_app.add_branch("main")
        main.add_environment("BUILD_ENV", "production")

        dev = amplify_app.add_branch("staging",
                                     performance_mode=True
                                     )

        dev.add_environment("BUILD_ENV", "staging")
