class Bitset:
    def __init__(self, size: int):
        self.bit = 0
        self.size = size
        self.ct = 0

    def fix(self, idx: int) -> None:
        if self.bit&(1<<idx) == 0:
            self.bit = self.bit|(1<<idx)        
            self.ct+=1

    def unfix(self, idx: int) -> None:
        if self.bit&(1<<idx) != 0:
            mask = ~(1<<idx)
            self.bit = self.bit&mask
            self.ct-=1

    def flip(self) -> None:
        self.bit = ~self.bit
        self.ct = self.size - self.ct

    def all(self) -> bool:
        return self.size == self.ct
        
    def one(self) -> bool:
        return self.ct >= 1
        
    def count(self) -> int:
        return self.ct

    def toString(self) -> str:
        string = ''
        for i in range(self.size):
            if self.bit&(1<<i) != 0: 
                string+='1'
            else:
                string+='0'
        return string


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()