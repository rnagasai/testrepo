from queue import Queue

def reversequeue(q):
    stack=[]
    while(not q.empty()):
        stack.append(q.queue[0])
        q.get()
    while (len(stack)!=0):
        q.put(stack[-1])
        stack.pop()


q=Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
q.put(50)
reversequeue(q)

while(not q.empty()):
    print(q.queue[0],end=" ")
    q.get()
