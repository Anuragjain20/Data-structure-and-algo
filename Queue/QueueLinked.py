class Node:

    def __init__(self,data):
        self.data = data
        self.next = next



class QueueLL:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0      

    def enqueue(self,element):
        newNode = Node(element)

        if self.__head is None:
            self.__head = newNode

        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1

    def dequeue(self):
        if self.__count == 0:
            print("empty queue")
            return 

        ele = self.__head
        self.__head = ele.next
        dat = ele.data
        del ele
        self.__count -= 1
        return dat

    def isEmpty(self):
        return  self.__count == 0


    def size(self):
        return self.__count

    def front(self):
        if self.__count == 0:
            print("empty queue")
            return 

        return self.__head.data              



queue = QueueLL()
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)
while queue.isEmpty() is False:
    print(queue.dequeue())
