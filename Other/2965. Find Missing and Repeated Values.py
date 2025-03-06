class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        sum1, sum2 = 0 , 0
        m = set()
        l =[-1, -1]

        for i in range(1, len(grid)*len(grid)+1):
            sum1+=i

        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if (grid[i])[j] in m:
                    l[0] = (grid[i])[j]
                m.add((grid[i])[j])
                sum2+= (grid[i])[j]

        l[1] = sum1 - sum2 + l[0]

        return l
