import aws_cdk as core
import aws_cdk.assertions as assertions
from pytest import fixture, Mark
from cdk_example_with_tdd.cdk_example_with_tdd_stack import CdkExampleWithTddStack


@fixture(scope='session')
def template():
    test_stack = core.Stack()
    stack = CdkExampleWithTddStack(test_stack, 'cdk-example-with-tdd')
    return assertions.Template.from_stack(stack)


def test_dynamodb_table(template):
    template.resource_count_is('AWS::DynamoDB::Table', 1)
    template.has_resource('AWS::DynamoDB::Table', { 'DeletionPolicy': 'Delete' })