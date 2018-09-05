class Solution:
    def candy(self, ratings):
        c = 0
        p = [1]*len(ratings)
        l = [1]*len(ratings)
        le = len(ratings)
        for i in range(len(ratings)):
            if i != 0:
                if ratings[i-1] > ratings[i] and p[i-1] <= p[i]:
                    p[i-1] += p[i] - p[i-1] + 1
                elif ratings[i-1] < ratings[i] and p[i-1] >= p[i]:
                    p[i] += p[i-1] - p[i] + 1
            
            if i != (len(ratings) -1):
                if ratings[le - i - 1] < ratings[le - i - 2] and l[le - i - 1] >= l[le - i - 2]:
                    l[le - i - 2] += l[le - i - 1] - l[le - i - 2] + 1
                elif ratings[le - i - 1] > ratings[le - i - 2] and l[le - i - 1] <= l[le - i - 2]:
                    l[le - i - 1] += l[le - i - 2] - l[le - i - 1] + 1           
        ret = 0
        for i in range(le):
            ret += max(p[i],l[i])
        return ret
 
        
        """
        :type ratings: List[int]
        :rtype: int
        """
