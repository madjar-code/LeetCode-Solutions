import unittest
from unittest import TestCase
from typing import (
    List,
    NamedTuple
)


class TwoPaths(NamedTuple):
    initial_path: str
    simply_path: str


class TestUnixPath(TestCase):
    def setUp(self) -> None:
        self.paths = [
            TwoPaths(
                initial_path='/home/',
                simply_path='/home'
            ),
            TwoPaths(
                initial_path='/../',
                simply_path='/'
            ),
            TwoPaths(
                initial_path='/home//foo',
                simply_path='/home/foo'
            )
        ]

    def test_correct_data(self) -> None:
        for two_paths in self.paths:
            unix_path = UnixPath(two_paths.initial_path)
            result_path = unix_path.simplified_path
            self.assertEqual(result_path, two_paths.simply_path)
        

class UnixPath:
    SEP = '/'
    CURRENT_DIR = '.'
    PARENT_DIR = '..'

    def __init__(self, path: str) -> None:
        self.path = path
        self.dir_stack: List[str] = []

    @property
    def simplified_path(self) -> str:
        for dir in self.path.split(self.SEP):
            if dir == self.CURRENT_DIR or not dir:
                continue

            if dir == self.PARENT_DIR:
                if self.dir_stack:
                    self.dir_stack.pop()
            else:
                self.dir_stack.append(dir)
        return self.SEP + self.SEP.join(self.dir_stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        return UnixPath(path).simplified_path


if __name__ == '__main__':
    unittest.main()
