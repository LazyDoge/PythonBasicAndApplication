class ExtendedStack(list):
    def check(self):
        return len(self) >= 2

    def sum(self):
        if self.check():
            self.append(self.pop() + self.pop())

    def sub(self):
        if self.check():
            self.append(self.pop() - self.pop())

    def mul(self):
        if self.check():
            self.append(self.pop() * self.pop())

    def div(self):
        if self.check():
            self.append(self.pop() // self.pop())


lissst = ExtendedStack()
lissst.append(1)
lissst.append(2)
lissst.append(3)
lissst.append(4)
lissst.append(5)

tmp = lissst
print(tmp)

print(tmp.sum())

tmp = lissst


print(tmp.sub())


tmp = lissst

print(tmp.mul())

tmp = lissst

print(tmp.div())

print(tmp)