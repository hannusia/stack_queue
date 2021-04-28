"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack
import copy


def queue_to_stack(queue):
    """
    Convert a queue to a stack using another stack
    """
    input_queue = copy.deepcopy(queue)
    output_stack = ArrayStack()
    converter_stack = ArrayStack()
    # Get the queue items
    while True:
        try:
            converter_stack.push(input_queue.pop())
        except KeyError:
            break
    # Reverse the queue
    while True:
        try:
            output_stack.push(converter_stack.pop())
        except KeyError:
            break
    return output_stack
