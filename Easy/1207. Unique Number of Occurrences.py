class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        countSet = set()

        for i in range(len(arr)):
            map[arr[i]] = 1 + map.get(arr[i], 0)

        for i in map:
            if map[i] in countSet:
                return False
            else:
                countSet.add(map[i])
        return True