class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._last_print_ts = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        last_ts = self._last_print_ts.get(message)
        if last_ts is None or timestamp - last_ts >= 10:
            self._last_print_ts[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
