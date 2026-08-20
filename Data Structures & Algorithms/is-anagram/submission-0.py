class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            sl = list(s);
            tl = list(t);
            return sl.sort() == tl.sort();
        """
        return sorted(s) == sorted(t);