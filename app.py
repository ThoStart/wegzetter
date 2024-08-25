import os

import aws_cdk as cdk

from infra.wegzetter_stack import WegzetterStack


app = cdk.App()
WegzetterStack(app, "WegzetterStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    )

app.synth()
