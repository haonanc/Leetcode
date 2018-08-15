class Solution(object):
    def isPalindrome(self, s):
        s = s.upper()
        l,r = 0,len(s)-1
        while(l <= r):

            while True:
                if s[l].isalpha() or  s[l].isdigit() or l + 1 > r:
                    break
                l += 1
                
            while True:
                if s[r].isalpha() or  s[r].isdigit() or l > r -1 :
                    break
                r -= 1 
                
            if s[l] != s[r]:
                return False  
            l += 1
            r -= 1
        return True
        """
        :type s: str
        :rtype: bool
        """
        
