class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.rsplit(maxsplit=1)[-1]
        return len(last)