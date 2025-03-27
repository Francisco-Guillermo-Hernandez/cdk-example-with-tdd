from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_dynamodb as DynamoDB,
    RemovalPolicy,

    aws_lambda as Lambda,
    aws_iam as Iam,
    Duration
)
from constructs import Construct

class CdkExampleWithTddStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table_name = 'Whether'
        table = DynamoDB.Table(
            self, 
            table_name, 
            partition_key=DynamoDB.Attribute(
                name='ZipCode', 
                type=DynamoDB.AttributeType.STRING,
            ), 
            removal_policy=RemovalPolicy.DESTROY
        )

        # Create a Lambda function and load the code from
        insertion_lambda = Lambda.Function(
            self, 
            'InsertionLambda',
            runtime=Lambda.Runtime.PYTHON_3_9,
            handler='index.handler',
            code=Lambda.Code.from_asset('lambda'),
            timeout=Duration.seconds(300),
            memory_size=256,
            environment={
                'TABLE_NAME': table.table_name
            }
        )

        # Add a policy to write records into dynamodb
        insertion_lambda.add_to_role_policy(Iam.PolicyStatement(
            actions=['dynamodb:BatchWriteItem'],
            resources=[table.table_arn]
        ))
        
        # Grant permissions to write data into dynamoDB
        table.grant_write_data(insertion_lambda)

      