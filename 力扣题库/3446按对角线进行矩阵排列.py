class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        '''双指针'''
        left = 0
        right = k-1
        flag = True
        sl = [i for i in s]
        while flag:
            '''
            判断条件
            '''
            if right > len(s):
                return ''.join(sl)
                break
            elif left > len(s):
                left = len(s)
            '''
            操作
            '''
            if k%2:#如果k奇数
                mid = (right+left)//2+1
                for i in range(left,mid-1):
                    j = mid + (mid-left)
                    sl[i] = s[j]
                    sl[j] = s[i]
            else:
                mid = (right+left)//2
                for i in range(left,mid+1):
                    j = mid+1 + (mid+1-left)
                    sl[i] = s[j]
                    sl[j] = s[i]
            '''
            更新
            '''
            right = right + 2*k
            left =  left + 2*k
s = "abcd"
k = 4
print(Solution().reverseStr(s,k))