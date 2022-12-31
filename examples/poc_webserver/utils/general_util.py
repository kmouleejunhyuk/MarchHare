from utils.kubernetes_util import create_pod

INPUT_THRESHOLD = 5


def create_input(names: list):
    result = []
    for i in range(0, len(names), INPUT_THRESHOLD):
        result.append(names[i:i+INPUT_THRESHOLD])


def schedule(names: list):
    podlist = []
    inputlist = create_input(names)

    for _ in range(len(names) // INPUT_THRESHOLD + 1):
        podlist.append(create_pod())

    return podlist, inputlist
