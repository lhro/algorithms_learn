

class dynamic:
    def __init__(self):
        self.x=0
        self.memo = [-1 for i in range(self.x+1)]
        self.memo[0]=0
        self.operate=[-1 for i in range(self.x+1)]
        self.operate[0]=0
        self.currency=(0,1,2,5,10,50,100)         

    def OPT(self,x):
        if x<0:
            return 99999999
        if self.memo[x]>=0:
            return self.memo[x]
        sum=99999999
        temp=0
        for c in self.currency[1:][::-1]:#切片+反转
            temp = self.OPT(x-c)+1
            if temp<sum:
                sum = temp
                self.operate[x]=c
                self.memo[x]=sum
        return sum

    def run(self,x):
        self.x=x
        self.memo = [-1 for i in range(self.x+1)]
        self.memo[0]=0
        self.operate=[-1 for i in range(self.x+1)]
        self.operate[0]=0
        self.OPT(x)

    def printoperate(self,x):
        if x==0:
            return
        print(self.operate[x],end=',')
        self.printoperate(x-self.operate[x])

    def greedy_verify(self,x):
        if x==0:
            return True
        temp = 0
        for c in self.currency[::-1]:
            if x>=c:
                temp = c
                break
        if temp == self.operate[x]:
            return self.greedy_verify(x-self.operate[x])
        else:
            return False

x=int(input('请输入零钱金额：'))
d = dynamic()
d.run(x)
d.printoperate(x)
print(d.greedy_verify(x))

for x in range(1000):
    d.run(x)
    print(x,':',d.greedy_verify(x))



