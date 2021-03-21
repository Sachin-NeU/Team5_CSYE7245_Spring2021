#### Model - MobileNet (CNN) 
- Depthwise Separable Convolution is used to reduce the model size and complexity. It is particularly useful for mobile and embedded vision applications
- The model can be used in edge devices such as IoT devices or mobile applications - owing to its small size.

#### Continuous Model Integration

- Made possible by chaining all processes using Airflow
- The pipeline can be scheduled to run at a predefined cadence and is constantly retraining the model
- Continuously upload the trained graph and labels to S3

![pipeline](/airflow_cnn_pipeline/img/airflow.jpg)

### Training Pipeline

Airflow is a platform to programmatically author, schedule and monitor workflows.
Use airflow to author workflows as directed acyclic graphs (DAGs) of tasks. 

The airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed. [1]

### Requirements

Install the dependencies as outlined in the `requirements.txt` by running
```
pip install -r requirements.txt
```
#### Update S3 Bucket details

Provide the S3 bucket name in the `bucket_name` parameter in `s3_uploader/upload_models.py`

#### Airflow Configuration

Once Airflow is installed, configure the same by running:

```
# Use your present working directory as
# the airflow home
export AIRFLOW_HOME=~(pwd)

# export Python Path to allow use
# of custom modules by Airflow
export PYTHONPATH="${PYTHONPATH}:${AIRFLOW_HOME}"


# initialize the database
airflow db init

airflow users create \
    --username admin \
    --firstname <YourName> \
    --lastname <YourLastName> \
    --role Admin \
    --email example@example.com
```

#### Using Airflow

Start the Airflow server in daemon
```
airflow webserver -D
```
Start the Airflow Scheduler
```
airflow scheduler
```

Once both are running - you should be able to access the Airflow UI by visiting http://127.0.0.1:8080/home on your browser.


Kill the process by running `kill <PID>` - in this case, it would be `kill 13280`

### Running the Pipeline

Login to Airflow on your browser and turn on the `CNN-Training-Pipeline` DAG from the UI. Start the pipeline by choosing the DAG and clicking on Run.

![airflow_run](/airflow_cnn_pipeline/img/airflow_ui.gif)


###Clad Document

https://docs.google.com/document/d/1tbpSaO3b8s1K2is9f7G_6I91MYg_-PmIPo2QzDscLas/edit
