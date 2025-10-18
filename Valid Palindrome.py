class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.sub(r'[^a-zA-Z0-9]', '', s)
        l,r = 0, len(ss)-1
        while l<r:
            if ss[l].lower()!=ss[r].lower():
                return False
            l+=1
            r-=1
        else:
            return True
