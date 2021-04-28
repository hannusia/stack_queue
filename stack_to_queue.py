"""
Stack to queue converter.
"""

from arraystack import ArrayStack
from arrayqueue import ArrayQueue
import copy


def stack_to_queue(stack):
    """
    Convert queue to a stack
    """
    input_stack = copy.deepcopy(stack)
    output_queue = ArrayQueue()
    while True:
        try:
            output_queue.add(input_stack.pop())
        except KeyError:
            break
    return output_queue
