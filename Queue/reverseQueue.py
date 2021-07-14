from queue import Queue

def reverse_queue(q):
    if q.empty() == True:
        return q

    e = q.get()
    q = reverse_queue(q)
    q.put(e)
    return q


q = Queue()
for i in range(10,40,10):
    
    q.put(i)


q = reverse_queue(q)


for i in range(10):
    print(q.get())