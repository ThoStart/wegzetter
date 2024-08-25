import aws_cdk as core
import aws_cdk.assertions as assertions

from infra.wegzetter_stack import WegzetterStack

# example tests. To run these tests, uncomment this file along with the example
# resource in infra/wegzetter_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WegzetterStack(app, "infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
