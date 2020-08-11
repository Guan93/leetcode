# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:


class Solution:
    def __init__(self):
        self.left = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        n_left_read = 0
        n_left = len(self.left)
        if n_left > 0:
            n_left_read = min(n, n_left)
            buf[:n_left_read] = self.left[:n_left_read]
            self.left = self.left[n_left_read:]
        if len(self.left) > 0:
            return n_left_read

        num_read = n_left_read
        num_read4 = 4
        buf4 = None
        while num_read < n and num_read4 == 4:
            buf4 = [None] * 4
            num_read4 = min(read4(buf4), n - num_read)
            buf[num_read:num_read + num_read4] = buf4[:num_read4]
            num_read += num_read4
        if buf4:
            self.left = [el for el in buf4[num_read4:] if el]
        return num_read