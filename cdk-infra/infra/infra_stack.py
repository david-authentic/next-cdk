from aws_cdk import (
    Stack,
    aws_amplify
)
from constructs import Construct

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        amplify = amplify.CfnApp(
            self, "Nextjs",
            name="NextjsApp",
            repository="https://github.com/david-authentic/nextjs-cdk.git",
            oauth_token="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",
            build_spec="amplify.yml",
            environment_variables=[{}]
        )
