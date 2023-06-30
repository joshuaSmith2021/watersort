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

    def is_complete(self) -> bool:
        return (self.is_empty()
                or len(set(self.contents)) == 1
                and len(self.contents) == self.capacity)


def move_possible(src: Tube, dest: Tube) -> bool:
    '''
    Return True if at least the top layer of src can be moved to dest. Return
    False otherwise.
    '''

    return (not src.is_empty()
           and not dest.is_full()
           and (src.peek() == dest.peek() or dest.is_empty()))


def tube_dump(src: Tube, dest: Tube) -> int:
    '''
    Dump as much of src as possible into dest and return the number of colors
    moved.
    '''

    i = 0
    while move_possible(src, dest):
        dest.push(src.pop())
        i += 1

    return i


class Level:
    tubes: List[Tube]

    def __init__(self, tubes: List[Tube]) -> None:
        self.tubes = tubes

    def possible_moves(self):
        '''
        Generate tuples of integers of the form (int, int), where index 0
        is the source tube and index 1 the destination tube.
        '''

        for src in range(len(self.tubes) - 1):
            for dest in range(src + 1, len(self.tubes)):
                if move_possible(self.tubes[src], self.tubes[dest]):
                    yield (src, dest)
