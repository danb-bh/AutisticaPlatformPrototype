#!/usr/bin/env python3

from aws_cdk import core

from deployment_pipeline.deployment_pipeline_stack import DeploymentPipelineStack


app = core.App()
DeploymentPipelineStack(app, "deployment-pipeline")

app.synth()
