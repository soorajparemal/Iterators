class me:
     def __init__(self,age):
             self.age=age
     def __iter__(self):
             return self
     def next(self):
             if (self.age) != 0:
                 self.age += 20
                 return self.age
             else :
                raise StopIteration
