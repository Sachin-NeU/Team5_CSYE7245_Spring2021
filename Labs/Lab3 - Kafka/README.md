## Apache Kafka


#### What is Kafka?
Kafka is a Distributed Streaming Publish-Subscribe messaging platform capable of handling millions of messages per minute.
Apache Kafka was originally developed by LinkedIn, and was subsequently open-sourced in early 2011.


#### USE CASES OF KAFKA
#### Kafka Messaging
Kafka is a distributed large-scale publish-subscribe message processing applications.
####Website Activity Tracking
To be able to rebuild a user activity tracking pipeline as a set of real-time publish-subscribe feeds, it is the original Use Case for Kafka.
####Kafka Metrics
For operational monitoring data, to produce centralized feeds of operational data, it includes aggregating statistics from distributed applications.
####Kafka Log Aggregation
In order to collect logs from multiple services and make them available in a standard format to multiple consumers, we can use Kafka across an organization.
####Stream Processing
Many users of Kafka process data in processing pipelines consisting of multiple stages, where raw input data is consumed from Kafka topics and then aggregated, enriched, or otherwise transformed into new topics for further consumption or follow-up processing.
####Commit Log
While it comes to a distributed system, Kafka can serve as a kind of external commit-log for it. Generally, it replicates data between nodes. Also, acts as a re-syncing mechanism for failed nodes to restore their data. The feature of log compaction in Kafka helps to support this usage.

### Getting Started

#### Download & Configure Kafka
- Download Apache Kafka from [here](https://kafka.apache.org/downloads)
- Unzip contents of the downloaded file

#### Python Libraries 

- kafka-python - Install the Python client for the Apache Kafka by running `pip3 install kafka-python`. 


#### Starting Zookeeper & Kafka Broker

Navigate to the directory where the downloaded files are unzipped and start the Zookeeper service:
```
C:\kafka\bin\windows\zookeeper-server-start.bat C:\kafka\config\zookeeper.properties
```
Additionally, start the Kafka broker by running:
```
C:\kafka\bin\windows\kafka-server-start.bat C:\kafka\config\server.properties
```

### Usage

Once the Zookeeper and Kafka broker services are started, we can use the Python scripts on this repo.

#### Using `producer.py`
Run the script to publish events to the newly created topic `sample`

#### Using `consumer.py`
Run the script to consume the events published by the producer. This script should write messages to the console.


### Usage

Use the `twitter-stream.py` script to fetch tweets using Twitter's API in real-time. Ensure that you enter your bearer token in the script under the `BEARER_TOKEN` param. This script:
- Fetches sampled tweets in real-time.
  
- Publishes these tweets to the Kafka Broker

On running `consumer.py` - you should see all the published events, that are collected by the consumer. 