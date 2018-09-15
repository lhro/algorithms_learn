from enum import Enum

OPT = Enum('OPT',('Equal','Jsub','Isub','Stop'))

class LCS:
    def __init__(self):
        self.c=list()#备忘录
        self.b=list()#操作备忘录
        self.x=str()
        self.y=str()
        self.lcs=str()

    def __init(self,x,y):
        self.x = x
        self.y = y
        self.c = [[0 for j in range(0,len(y)+1)] for i in range(0,len(x)+1)]#i+1行j+1列
        self.b = [[OPT.Stop for j in range(0,len(y)+1)] for i in range(0,len(x)+1)]

    def opt(self):
        for i in range(1,len(self.x)+1):
            for j in range(1,len(self.y)+1):
                if self.x[i-1] == self.y[j-1]:
                    self.c[i][j] = self.c[i-1][j-1]+1
                    self.b[i][j] = OPT.Equal
                elif self.c[i][j-1] < self.c[i-1][j]:
                    self.c[i][j] = self.c[i-1][j]
                    self.b[i][j] = OPT.Isub
                else:
                    self.c[i][j] = self.c[i][j-1]
                    self.b[i][j] = OPT.Jsub

    def printSub(self,i,j):
        if OPT.Stop == self.b[i][j]:
            return
        if self.b[i][j] == OPT.Equal:
            self.printSub(i-1,j-1)
            self.lcs+=self.x[i-1]
        elif self.b[i][j] == OPT.Isub:
            self.printSub(i-1,j)
        else:
            self.printSub(i,j-1)

    def run(self,x,y):
        self.__init(x,y)
        self.opt()
        self.printSub(len(self.x),len(self.y))
        print('Length of LCS:',self.c[len(self.x)][len(self.y)])
        print('LCS:',self.lcs)
        print('c[][]:')
        for e in self.c:
            print(e)
        print('b[][]:')
        for e in self.b:
            for ee in e:
                print(ee.name,end=' ')
            print()

l = LCS()
x = str(input('First string:'))
y = str(input('Second string:'))
l.run(x,y)
