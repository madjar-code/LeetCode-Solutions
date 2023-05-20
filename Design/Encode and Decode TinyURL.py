from typing import (
    Dict
)
from random import choice
from string import ascii_letters, digits

SIZE = 7
AVAIABLE_CHARS = ascii_letters + digits


class Codec:
    def __init__(self) -> None:
        self.URL_map: Dict[str, str] = {}
        self.prefix = 'http://tinyurl.com'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL"""
        short_url: str = self.prefix + self._random_code()
        if short_url in self.URL_map:
            self.encode(longUrl)
        self.URL_map[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        if shortUrl not in self.URL_map:
            raise KeyError('No short URL')
        return self.URL_map[shortUrl]

    @staticmethod
    def _random_code(chars=AVAIABLE_CHARS):
        """Random symbol code generation"""
        return ''.join([choice(chars) for _ in range(SIZE)])