from typing import List


class Tube:
    capacity: int
    contents: List[int]

    def __init__(self, capacity: int, contents: List[int]):
        assert capacity >= len(contents)
        self.capacity = capacity
        self.contents = contents

    def peek(self) -> int:
        if len(self.contents) == 0:
            return None

        return self.contents[-1]

    def pop(self) -> int:
        if len(self.contents) == 0:
            return None

        return self.contents.pop()

    def push(self, color: int):
        # Ensure tube has space and the color matches the top color
        assert len(self.contents) < self.capacity
        assert self.is_empty() or color == self.peek()
        self.contents.append(color)

    def is_full(self) -> bool:
        return self.capacity == len(self.contents)

    def is_empty(self) -> bool:
        return len(self.contents) == 0


def tube_dump(src: Tube, dest: Tube) -> int:
    '''
    Dump as much of src as possible into dest and return the number of colors
    moved.
    '''

    i = 0
    while (not src.is_empty()
           and not dest.is_full()
           and src.peek() == dest.peek() or dest.is_empty()):
        dest.push(src.pop())
        i += 1

    return i
