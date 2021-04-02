from diagrams import Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import SimpleStorageServiceS3Bucket as S3
from diagrams.saas.analytics import Snowflake
from diagrams.onprem.client import Client
from diagrams.onprem.client import User
from diagrams.onprem.client import Users
from diagrams.oci.devops import APIService
from diagrams.oci.devops import APIGateway

graph_attr = {
    "fontsize": "16",
    "bgcolor": "white"
}

#disable automatic file opening by passing show=False
with Diagram("Moody's architecture", show=False, graph_attr=graph_attr):
    User('User') >> Client("App") >> APIGateway("API AUthenication") >> \
    Edge(label="request/response") << APIService("API Service")
