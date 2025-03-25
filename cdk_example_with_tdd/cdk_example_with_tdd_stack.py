from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_dynamodb as DynamoDB,
    RemovalPolicy,
)
from constructs import Construct

class CdkExampleWithTddStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table_name = 'Wheater'
        table = DynamoDB.Table(
            self, 
            table_name, 
            partition_key=DynamoDB.Attribute(
                name='ZipCode', 
                type=DynamoDB.AttributeType.STRING,
            ), 
            removal_policy=RemovalPolicy.DESTROY
        )

      