class Solution:

    def isVowel(self, s: str ) -> bool:
        if s.lower() in ('a', 'e', 'i', 'o', 'u'):
            return True
        else:
            return False

    def reverseVowels(self, s: str) -> str:
        out = ""
        vowels = list()
        for i in range(len(s)):
            if self.isVowel(s[i]):
                vowels.append(s[i])

        j = len(vowels) - 1
        for i in range(len(s)):
            if self.isVowel(s[i]):
                out = out + vowels[j]
                j -= 1
            else:
                out = out + s[i]
        return out