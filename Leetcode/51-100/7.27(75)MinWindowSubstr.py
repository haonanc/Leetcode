class Solution:
    def minWindow(self, s, t):
        a = list(range(0,127))
        dic = {i:0 for i in a}
        for char in t:
            print(ord(char))
            dic[ord(char)] += 1
        head, tail = 0,0
        d = 99999
        start = 0
        counter = len(t)
        while(head<len(s) and tail < len(s)):
            if dic[ord(s[head])] > 0:
                counter -= 1
            dic[ord(s[head])] -=1
            head +=1
            while counter == 0:
                if(d>head - tail):
                    d = head -tail
                    start = tail
                if dic[ord(s[tail])] == 0:
                    counter += 1
                dic[ord(s[tail])] +=1     
                tail +=1
        if(d == 99999):
            return ""
        return s[start:start+d]
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
