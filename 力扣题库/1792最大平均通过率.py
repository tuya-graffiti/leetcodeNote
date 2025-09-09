from heapq import *
'''
数据结构类题目用class写
'''
class Entry:
    __slots__ = 'p','t'
    def __init__(self,p,t):
        self.p = p
        self.t = t
    def __lt__(self,b:'Entry'):# 魔术方法小于比较操作 用于自定义对象之间的比较规则
        return (self.t - self.p)*b.t*(b.t + 1)>(b.t - b.p)*self.t*(self.t + 1)
    # 数学推导
class Solution:
    def maxAverageRatio(self,classes,extraStudents):
        h = [Entry(*c) for c in classes] # 解包操作符
        heapify(h) # 将列表转化为最小堆
        for _ in range(extraStudents):
            heapreplace(h,Entry(h[0].p +1 , h[0].t+1))
        return sum(e.p / e.t for e in h)/len(h)
print(Solution().maxAverageRatio([[1,2],[3,5],[2,2],[3,4]], 2))