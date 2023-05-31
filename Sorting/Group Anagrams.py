from typing import (
    TypeAlias,
    List,
)


CharType: TypeAlias = str

class AnagramGroup:
    def __init__(self, initial_word: str) -> None:
        self._key: str = AnagramGroup._sort_chars(initial_word) 
        self._words_container: List[str] = [initial_word]

    @staticmethod
    def _sort_chars(word: str) -> str:
        sorted_word: str = sorted(word)
        return sorted_word
        # chars: List[CharType] = list(word)
    
        # length = len(word)
        # for i in range(length):
        #     for k in range(length - i - 1):
        #         if chars[k] > chars[k+1]:
        #             chars[k], chars[k+1] = chars[k+1], chars[k]

        # sorted_word: str = ''.join(chars)
        # return sorted_word

    def get_key(self) -> str:
        return self._key

    def get_list(self) -> List[str]:
        return self._words_container

    def is_group_part(self, word: str) -> bool:
        if AnagramGroup._sort_chars(word) == self._key:
            return True
        return False

    def add_word(self, word: str) -> bool:
        self._words_container.append(word)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: List[List[str]] = []
        groups: List[AnagramGroup] = []
        for string in strs:
            self._check_for_groups(string, groups)
        for group in groups:
            result.append(group.get_list())
        return result

    def _check_for_groups(self, word: str, groups: List[AnagramGroup]):
        for group in groups:
            if group.is_group_part(word):
                group.add_word(word)
                return
        groups.append(AnagramGroup(word))
