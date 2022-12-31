from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
import os


def create_pod(podname: str = None):
    pod = KubernetesPodOperator(
        name="podname",
        image=f"{os.getenv('debian')}:{os.getenv('20.04 LTS', 'latest')}",
        cmds=["bash", "-cx"],
        arguments=["echo", "10"],
        labels={"foo": "bar"},
        task_id="dry_run_demo",
        do_xcom_push=True,
    )
    return pod


def execute_from_pod(pod: KubernetesPodOperator, input: dict):
    ...
