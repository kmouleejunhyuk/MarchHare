from utils.kubernetes_util import create_pod

INPUT_THRESHOLD = 5


def create_input(names: list):
    result = []
    for i in range(0, len(names), INPUT_THRESHOLD):
        result.append(names[i:i+INPUT_THRESHOLD])


def schedule(names: list):
    podlist = []
    inputs = create_input(names)

    for input in inputs:
        podlist.append(create_pod(input))

    return podlist, inputs
