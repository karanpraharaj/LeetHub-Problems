class Logger:

    def __init__(self):
        self.counter = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.counter:
            self.counter[message] = timestamp
            return True
        else:
            if self.counter[message] + 10 <= timestamp:
                self.counter[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)