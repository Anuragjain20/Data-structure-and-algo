from queue import Queue

def reverseKqueue(q,k):
    if q.empty() == True or k > q.qsize():
        return

    if k<= 0:
        return

    stack = []   
    for i in range(k):
        stack.append(q.queue[0])  
        q.get()


    while len(stack) != 0:
        q.put(stack[-1])
        stack.pop()


    for i in range(q.qsize()- k ):
        q.put(q.queue[0])
        q.get()

q = Queue()
for i in range(10,40,3):
    
    q.put(i)


reverseKqueue(q,3)


for i in range(10):
    print(q.get())        