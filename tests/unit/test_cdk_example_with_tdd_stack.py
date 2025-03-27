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


def test_insertion_lambda(template):
    template.has_resource_properties('AWS::Lambda::Function', {
        'Runtime': 'python3.9',
        'Handler': 'index.handler',
        'Environment': {
            'Variables': assertions.Match.object_like({
                'TABLE_NAME': assertions.Match.any_value()
            })
        }
    })

    template.has_resource_properties('AWS::IAM::Policy', {
        'PolicyDocument': {
            'Statement': assertions.Match.array_with([
                {
                    'Action': 'dynamodb:BatchWriteItem',
                    'Effect': 'Allow',
                    'Resource': {
                        'Fn::GetAtt': [
                            assertions.Match.any_value(),
                            'Arn'
                        ]
                    },
                },
            ])
        },
    })