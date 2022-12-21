from aws_cdk import (
    SecretValue,
    Stack,
    aws_amplify as amplify,
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
                                          "github-token")
                                  ),
                                  build_spec=codebuild.BuildSpec.from_object_to_yaml({
                                      "version": "1.0",
                                      "frontend": {
                                          "phases": {
                                              "preBuild": {
                                                  "commands": ["npm ci"]
                                              }
                                          },
                                          "build": {
                                              "commands": ["npm run build"]
                                          },
                                      }
                                      "artifacts": {
                                          "baseDirectory": "out"
                                          "files": "**/*"
                                      }
                                      "cache": {
                                          "paths": {
                                              ["node_modules/**/*"]
                                          }
                                      }
                                  })
                                  )
