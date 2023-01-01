from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.api.client.local_client import Client
import os


def create_pod(input):
    pod = KubernetesPodOperator(
        name="podname",
        image=f"{os.getenv('debian')}:{os.getenv('20.04 LTS', 'latest')}",
        cmds=["bash", "-cx"],
        arguments=["echo", f"{input}"],
        labels={"foo": "bar"},
        task_id="dry_run_demo",
        do_xcom_push=True,
    )
    return pod


def execute_from_pod(pod: KubernetesPodOperator):
    try:
        c = Client(None, None)
        c.trigger_dag(dag_id='dry_run_demo', run_id='test_run_id', conf={})
        return 'completed'
    except Exception as e:
        return str(e)
