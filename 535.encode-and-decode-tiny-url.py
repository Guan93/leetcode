#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
import random


class Codec:
    def __init__(self):
        self.fixed_length = 6
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        self.map = dict()

    def _get_rand_key(self):
        return ''.join([
            self.alphabet[random.randint(0,
                                         len(self.alphabet) - 1)]
            for _ in range(self.fixed_length)
        ])

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self._get_rand_key()
        while key in self.map:
            key = self._get_rand_key()
        self.map[key] = longUrl
        return f"http://tinyurl.com/{key}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map.get(shortUrl[-self.fixed_length:])


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
