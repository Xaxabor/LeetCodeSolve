# class Solution:

#     def isVowel(self, s: str ) -> bool:
#         if s.lower() in ('a', 'e', 'i', 'o', 'u'):
#             return True
#         else:
#             return False

#     def reverseVowels(self, s: str) -> str:
#         out = ""
#         vowels = list()
#         for i in range(len(s)):
#             if self.isVowel(s[i]):
#                 vowels.append(s[i])

#         j = len(vowels) - 1
#         for i in range(len(s)):
#             if self.isVowel(s[i]):
#                 out = out + vowels[j]
#                 j -= 1
#             else:
#                 out = out + s[i]
#         return out
    
class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowel = "aeiouAEIOU"
        # tempvowel=[]
        # ans = []
        # for i in range(0, len(s)):
        #     if s[i] in vowel :
        #         tempvowel.append(s[i])

        # print(tempvowel)
        
        # for i in range(0, len(s)):
        #     if s[i] in vowel :
        #         ans.append(tempvowel.pop())
        #     else:
        #         ans.append(s[i])
        # return "".join(ans)

        # vowel = set("aeiouAEIOU")
        # l =  0
        # r = len(s)-1
        # s=list(s)
        # while(l<r):
        #     if(s[l] not in vowel and s[r] not in vowel):
        #         l=l+1
        #         r=r-1
        #     elif(s[l] in vowel and s[r] in vowel):
        #         s[l], s[r] = s[r],s[l]
        #         l=l+1
        #         r=r-1
        #     elif(s[l] in vowel and s[r] not in vowel):
        #         r=r-1
        #     elif(s[l] not in vowel and s[r] in vowel):
        #         l=l+1
        # return "".join(s)

        vowel = set("aeiouAEIOU")
        l =  0
        r = len(s)-1
        s=list(s)
        while(l<r):
            while l<r and s[l] not in vowel:
                l=l+1
            while l<r and s[r] not in vowel:
                r=r-1
            s[l], s[r] = s[r],s[l]
            l, r = l+1, r-1
        return "".join(s)