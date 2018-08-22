class Solution:
    def partition(self, s):
        ret = []
        backTrack(s,0,[],ret)
        return ret

        """
        :type s: str
        :rtype: List[List[str]]
        """
def backTrack(s,begin,l,ret):
    if begin == len(s):
        ret.append(copy.copy(l))
        return
    for i in range(len(s[begin:])):
        if check(s[begin:begin+i+1]):
            l.append(s[begin:begin+i+1])
            backTrack(s,begin+i+1,l,ret)
            l.pop()

def check(str):
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str)-1-i]:
            return False
    return True
