import pendulum
from datetime import datetime, timedelta
import glob
from PIL import Image
from numpy import asarray
import os

from airflow.models import DAG
from airflow.decorators import dag, task, kubernetispodexecuter
from airflow import Dataset


KST = pendulum.timezone("Asia/Seoul")

#senario
# print hello airflow in interval 10 seconds
INTERVAL = 100
args = {
    'owner': 'user_name',
}


@dag(
    dag_id='hello_airflow',
    default_args = args,
    description = 'example for kubernetispodexecuter',
    start_date = timedelta(seconds = 10),
    schedule = datetime,
)
def greeting():
    @task()
    def get_params():
        return "HELLO AIRFLOW! NICE TO MEET YOU"


    @task()
    def print_greeting(param_string):
        print(param_string)

    
    params = get_params()
    print_greeting(params)

check_img() 