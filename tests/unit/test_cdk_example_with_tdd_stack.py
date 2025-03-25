import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_example_with_tdd.cdk_example_with_tdd_stack import CdkExampleWithTddStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_example_with_tdd/cdk_example_with_tdd_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkExampleWithTddStack(app, "cdk-example-with-tdd")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
