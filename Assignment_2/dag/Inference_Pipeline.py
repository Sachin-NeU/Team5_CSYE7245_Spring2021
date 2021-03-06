from airflow import DAG
from airflow.operators.bash import BashOperator
#from airflow.operators import BashOperator,PythonOperator
from datetime import datetime, timedelta

seven_days_ago = datetime.combine(datetime.today() - timedelta(7),datetime.min.time())

default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': seven_days_ago,
        'email': ['airflow@airflow.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
      }

dag = DAG('inference', default_args=default_args)

t1 = BashOperator(
    task_id='inference',
    bash_command='python3 /home/user/.local/lib/python3.8/site-packages/airflow/pythonfiles/inference.py',
    dag=dag)
    
