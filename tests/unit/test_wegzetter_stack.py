import aws_cdk as core
import aws_cdk.assertions as assertions

from wegzetter.wegzetter_stack import WegzetterStack

# example tests. To run these tests, uncomment this file along with the example
# resource in wegzetter/wegzetter_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WegzetterStack(app, "wegzetter")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
