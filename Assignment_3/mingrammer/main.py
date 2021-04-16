from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import SimpleStorageServiceS3Bucket as S3
from diagrams.saas.analytics import Snowflake
from diagrams.generic.blank import Blank
from diagrams.onprem.client import User
from diagrams.oci.devops import APIService
from diagrams.oci.devops import APIGateway

graph_attr = {
    "fontsize": "20",
    "bgcolor": "lavenderblush"
}

#disable automatic file opening by passing show=False
with Diagram("Datalytics Inc. API pipeline", show=False, graph_attr=graph_attr,):
    with Cluster("DB Cluster"):
        sf = Snowflake("Snowflake")
        s3 = S3("S3 Bucket")
        db_master = [sf << Edge(color="darkbrown", label="load data") <<s3]

    with Cluster("API"):
        apiAuth = APIGateway("APIAuthentication")
        apiService = APIService("APIService")
        api = [apiAuth >> Edge(color="darkgreen", label="request/response") << apiService]

    User("User") >> \
        Edge(color="darkorange") \
        << apiAuth

    apiService>> Edge(color="darkgreen") \
         << sf
