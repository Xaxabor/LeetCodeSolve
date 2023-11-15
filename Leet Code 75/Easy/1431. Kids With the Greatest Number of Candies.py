class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        out = list()
        for i in range(len(candies)):
            if max < candies[i]:
                max = candies[i]

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max :
                out.append(True)
            else:
                out.append(False)

        return out