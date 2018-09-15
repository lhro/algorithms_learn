# Definition for a point.
class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        """
输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
        """
        points=list(set(points))
        if len(points)==0:
            return 0
        if len(points)==1:
            return 1
        if len(points)==2:
            return 2
        k_b=dict()
        x_c=dict()
        flag_xc=[]
        flag_kb=[]
        for m in range(1,len(points)):
            flag_kb.clear()
            flag_xc.clear()
            for n in range(0,m):
                i=points[m]
                j=points[n]

                if i.x == j.x:
                    if x_c.get(i.x)==None:
                        x_c[i.x]=2
                    else:
                        if i.x not in flag_xc:
                            x_c[i.x]=x_c[i.x]+1
                            flag_xc.append(i.x)
                else:
                    k=(i.y-j.y)/(i.x-j.x)
                    b=i.y-k*i.x
                    if k_b.get((k,b))==None:
                        k_b[(k,b)]=2
                    else:
                        if (k,b) not in flag_kb:
                            k_b[(k,b)]=k_b[(k,b)]+1
                            flag_kb.append((k,b))


        if len(k_b)==0:
            kb=0
        else:
            kb=max(k_b.values())
        if len(x_c)==0:
            xc=0
        else:
            xc=max(x_c.values())

        return max([kb,xc])

s = Solution()
#test=[Point(1,1),Point(3,2),Point(5,3),Point(4,1),Point(2,3),Point(1,4)]
#[[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]]
test=[]
for i in [[3,1],[12,3],[3,1],[-6,-1]]:
    test.append(Point(i[0],i[1]))
print(s.maxPoints(test))
