#from stackUsingArray import Stack
from stackUsingLL import Stack


s = Stack()
s.push(12)
s.push(13)
s.push(14)


while s.isEmpty() is False:
    print(s.pop())



#inbuilt
import queue
q = queue.LifoQueue()
q.put(12)
q.put(13)
q.put(14)
q.put(15)

while not q.empty():
    print(q.get())

