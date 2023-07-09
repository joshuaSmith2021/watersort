from __future__ import annotations

import json
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

    def push(self, color: int, force: bool = False):
        # Ensure tube has space and the color matches the top color
        assert len(self.contents) < self.capacity

        if not force:
            assert self.is_empty() or color == self.peek()

        self.contents.append(color)

    def is_full(self) -> bool:
        return self.capacity == len(self.contents)

    def is_empty(self) -> bool:
        return len(self.contents) == 0

    def is_homogenous(self) -> bool:
        return len(set(self.contents)) == 1

    def is_complete(self) -> bool:
        return (self.is_empty()
                or len(set(self.contents)) == 1
                and len(self.contents) == self.capacity)

    def __str__(self) -> str:
        return str(self.contents)

    __repr__ = __str__

    def to_csv(self) -> str:
        copy = [x for x in self.contents]
        while len(copy) < self.capacity:
            copy.append('')

        return ','.join(map(str, copy))

    @staticmethod
    def load_string(csv: str) -> Tube:
        elements = csv.split(',')
        stack = [int(x) for x in elements if x.isnumeric()]

        return Tube(len(elements), stack)


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

        for src in range(len(self.tubes)):
            if self.tubes[src].is_complete():
                continue

            for dest in range(len(self.tubes)):
                if src == dest:
                    continue

                if move_possible(self.tubes[src], self.tubes[dest]):
                    # Skip useless moves
                    if self.tubes[src].is_homogenous() and self.tubes[dest].is_empty():
                        continue

                    yield (src, dest)

    def is_complete(self) -> bool:
        return all(x.is_complete() for x in self.tubes)

    def __str__(self) -> str:
        return str(self.tubes)

    def dumps(self) -> str:
        return json.dumps([x.to_csv() for x in self.tubes])

    @staticmethod
    def loads(string: str) -> Level:
        tubes = [Tube.load_string(x) for x in json.loads(string)]
        return Level(tubes)


class Move:
    src: int
    dest: int
    n: int

    def __init__(self, src: int, dest: int, n: int) -> None:
        self.src = src
        self.dest = dest
        self.n = n

    def __str__(self) -> str:
        return f'{self.src} -> {self.dest}, n = {self.n}'

    __repr__ = __str__


def dfs(puzzle: str):
    stack = [puzzle]
    discovered = set()
    previous = {}

    final_state = None

    while stack:
        v = stack.pop()

        if v not in discovered:
            discovered.add(v)
            level = Level.loads(v)
            if level.is_complete():
                final_state = (v, 0, 0, 0)
                break

            moves = [x for x in level.possible_moves()]
            for src, dest in moves:
                level = Level.loads(v)
                n = tube_dump(level.tubes[src], level.tubes[dest])

                if level.dumps() not in discovered:
                    stack.append(level.dumps())
                    previous[level.dumps()] = (v, src, dest, n)

    path = []
    while final_state:
        path.append(final_state)
        final_state = previous.get(final_state[0], None)

    print('\n'.join(f'{x[1]} -> {x[2]} (n = {x[3]})' for x in path[::-1]))

