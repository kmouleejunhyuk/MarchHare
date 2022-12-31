import gradio as gr
from kubernetes.client import models as k8s
from utils.general_util import schedule
from utils.kubernetes_util import execute_from_pod

SERVICE_NAMESPACE = ''
RESOURCES = k8s.V1ResourceRequirements(
    limits={"memory": "1Gi", "cpu": "1"},
    requests={"memory": "500Mi", "cpu": "0.5"},
)


def service(name: str):
    # arbitary
    names = name.split(' ')
    pods_and_inputs = schedule(names)
    for (pod, input) in pods_and_inputs:
        execute_from_pod(pod, input)


if __name__ == '__main__':
    demo = gr.Interface(fn=service, inputs="text", outputs="text")
    demo.launch(share=True)
