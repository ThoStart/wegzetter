from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class WegzetterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC with default configurations
        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)

        # Create an ECS Cluster using Fargate as the launch type
        cluster = ecs.Cluster(self, "MyEcsCluster", vpc=vpc)

        # Create an ECR Repository to store Docker images
        repository = ecr.Repository(self, "MyEcrRepo")

        # Define a Fargate Task Definition
        task_definition = ecs.FargateTaskDefinition(self, "MyFargateTaskDef")

        # Add a container to the task definition
        container = task_definition.add_container("MyContainer",
            image=ecs.ContainerImage.from_asset("Dockerfile"),  # Replace with your Dockerfile path
            memory_limit_mib=512,  # Allocate 512 MiB of memory
            cpu=256  # Allocate 0.25 vCPU
        )

        # Map the container port to the task definition
        container.add_port_mappings(
            ecs.PortMapping(container_port=80, host_port=80)
        )

        # Create a Fargate Service with a load balancer
        ecs_patterns.ApplicationLoadBalancedFargateService(self, "MyFargateService",
            cluster=cluster,            # Specify the ECS cluster
            task_definition=task_definition,  # Use the Fargate task definition
            public_load_balancer=True  # Create a public-facing load balancer
        )
