
class RodCut:
    def __init__(self):
        self.p = [0,1,5,8,9,10,17,17,20,24,30]
        self.r =[]
        self.o=[]

    def cut(self,n):
        if self.r[n]>0:
            return self.r[n]
        if n == 0:
            self.r[0] = 0
            return 0
        q = -1
        for i in range(1,min(n+1,11)):
            m = self.p[i] + self.cut(n-i)
            if q < m:
                q = m
                self.o[n] = i
        self.r[n] = q
        return q

    def cut_b(self,n):
        self.r[0] = 0
        for i in range(1,n+1):
            for j in range(1,min(11,i+1)):
                m = self.p[j]+self.r[i-j]
                if self.r[i] < m:
                    self.r[i] = m
                    self.o[i] = j
        return self.r[n]

    def init(self,n):
        self.r = [-1 for i in range(n+1)]
        self.o = [-1 for i in range(n+1)]

    def print_operate(self,n):
        while n != 0:
            print(self.o[n],end = '\t')
            n -= self.o[n]

    def run(self,n):
        self.init(n)
        q = self.cut_b(n)
        print('max profit:',q)
        print('sub-rob:')
        self.print_operate(n)
        print()

while True:
    rr = RodCut()
    n = int(input('length:'))
    rr.run(n)


    