from stackUsingLL import Stack




def stockSpan(price):

    if len(price) >0:
        s = Stack()
        s.push(0)
        ij = [0]*len(price)
        ij[0] = 1
        for i in range(1,len(price)):
            while s.isEmpty() == False and price[s.top()] < price[i]:
                s.pop()

            ij[i] = i + 1 if s.isEmpty() else i - s.top()
            s.push(i)
        return ij


n = [60, 70, 80, 100, 90, 75, 80 ,120]    
k = [10,10,10,10]
print(stockSpan(n))
print(stockSpan(k))