from aws_cdk import (core,
                     aws_codepipeline as cp,
                     aws_codepipeline_actions as cpa)


class DeploymentPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_artifact = cp.Artifact()
        cloud_assembly_artifact = cp.Artifact()

        pipeline = c
