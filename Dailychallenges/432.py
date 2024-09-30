class AllOne:
    def __init__(self):
        self.one = {}
        self.minKey = ""
        self.maxKey = ""

    def inc(self, key: str) -> None:
        if key in self.one:
            self.one[key] += 1
        else:
            self.one[key] = 1

    def dec(self, key: str) -> None:
        if key in self.one:
            self.one[key] -= 1
            if self.one[key] == 0:
                del self.one[key]
        else:
            return

    def getMaxKey(self) -> str:
        self.maxKey = max(self.one, key=self.one.get, default="")
        return self.maxKey

    def getMinKey(self) -> str:
        self.minKey = min(self.one, key=self.one.get, default="")
        return self.minKey


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
