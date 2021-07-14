class QueueStack:
    

    def __init__(self):
        self.__s1 = []
        self.__s2 = []


    def enqueue(self,data):
        if self.__s1 == []:
            self.__s1.append(data) 
            return
        while self.__s1 != []:
            r= self.__s1.pop()
            self.__s2.append(r)

        self.__s1.append(data)

        while self.__s2 != []:
            r= self.__s2.pop()
            self.__s1.append(r)                   

    def dequeue(self):
        if self.__s1 == []:
            print("empty queue")
            return
        return self.__s1.pop()

    def front(self):
        if self.__s1 == []:
            print("empty queue")
            return
        return self.__s1[-1]   


    def size(self):
        return len(self.__s1)

    def isEmpty(self): 
        return len(self.__s1) == 0       



st = QueueStack()
st.enqueue(10)
st.enqueue(11)
st.enqueue(12)
st.enqueue(13) 

while st.isEmpty() == False:
    print(st.dequeue())