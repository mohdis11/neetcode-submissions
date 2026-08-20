class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0
        s = s.lower();
        while l < r:
            if not (s[l].isalnum()):
                l += 1;
            if not (s[r].isalnum()):
                r -= 1;

            if s[l] != s[r]:
                return False;
            r -= 1;
            l += 1;
        return True;



        


        