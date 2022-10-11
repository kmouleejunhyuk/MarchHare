import pendulum
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


KST = pendulum.timezone("Asia/Seoul")
args = {'owner': 'user_name'}

def dummy(name, age, ti):
    """Dummy function for example DAG

    Args:
        name (str): name
        age (str): age
        ti (Taskinstance): dummy for manual xcom push
    """
    xcom_arg = ti.xcoms_pull(task_ids='dummy')
    print(f'dummy is {name}, {age} old')

    ti.xcom_push(key='k1', value='jerry')


def get_xcom(dum, ti):
    """xcom example function

    Args:
        dum (NoneType): None, any arguments can be added in this position
        ti (Taskinstance): xcoms task input, must be named to ti
    """
    xcom_arg = ti.xcom_pull(task_ids='dummy', key = 'k1')
    print(xcom_arg)

with DAG(
    dag_id='my_dag',
    default_args = args,
    description = 'example dag',
    start_date=datetime(2022, 10, 10, tzinfo=KST),
    schedule_interval='@daily'
) as dag:

    task1 = PythonOperator(
        task_id='dummy',
        python_callable=dummy, # callable object
        op_kwargs={'name': 'Tom', 'age': 20}
    )

    task2 = PythonOperator(
        task_id='get_xcom',
        python_callable=get_xcom, # callable object
    )

    [task1] >> task2

## or

# from airflow.decorators import dag, task
# @dag(
#     dag_id='my_dag',
#     default_args = args,
#     description = 'example dag',
#     start_date=datetime(2022, 10, 10, tzinfo=KST),
#     schedule_interval='@daily'
# )

# def hello_world():
#     @task(multiple_outputs = True)
#     def dummy(name, age):
#         return {
#             'name': name, 
#             'age': age
#         }

#     @task()
#     def get_xcom(xargs):
#         print(xargs['name'], xargs['age'])

#     xargs = dummy('Tom', '19')
#     get_xcom(xargs)

# out = hello_world() 