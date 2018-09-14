class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    count += 1 
                    convert(grid,y,x)
        return count
    
    
def convert(grid,y,x): 
    if grid[y][x] == '1':
        grid[y][x] = '2'
        if x + 1 < len(grid[0]):
            convert(grid,y,x+1)
        if x - 1 >= 0:
            convert(grid,y,x-1)
        if y + 1 < len(grid):
            convert(grid,y+1,x)
        if y - 1 >= 0:
            convert(grid,y-1,x)
    
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
