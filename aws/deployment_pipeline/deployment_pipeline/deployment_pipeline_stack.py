from aws_cdk import (core as c,
                     pipelines as p,
                     aws_codepipeline as cp,
                     aws_codepipeline_actions as cpa)


def create_name(suffix: str) -> str:
    return "autistica-prototype-" + suffix


class DeploymentPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_artifact = cp.Artifact()
        cloud_assembly_artifact = cp.Artifact()

        pipeline_name = create_name('pipeline')
        pipeline = p.CdkPipeline(
            self,
            pipeline_name,
            pipeline_name=pipeline_name,
            cloud_assembly_artifact=cloud_assembly_artifact,
            source_action=cpa.GitHubSourceAction(
                action_name=create_name('github'),
                output=source_artifact,
                oauth_token=c.SecretValue.secrets_manager('github-token-for-account-danb-bh'),
                owner='danb-bh',
                repo='AutisticaPlatformPrototype',
                branch='danb'
            )
        )
