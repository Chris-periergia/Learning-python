#  Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
# The iterator should stop when it reaches a limit defined in the constructor.

class fib_iterator:
    def __init__(self,limit):
        self.limit=limit

    def __iter__(self):
        self.count=0
        self.prev=0
        self.next=1
        return self
    
    def __next__(self):
        if self.count>=self.limit:
            raise StopIteration
        self.count+=1
        self.next+=self.prev
        self.prev=self.next-self.prev
        return self.next
    
fib=fib_iterator(11)
itr=iter(fib)

for x in itr:
    print(next(itr))