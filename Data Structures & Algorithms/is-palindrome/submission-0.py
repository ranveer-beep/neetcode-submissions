class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        for r in range(len(s)):
            for q in range(len(s) - 1, -1, -1):
                if r < q:
                    if s[r] != s[q]:
                        return False
                    r += 1
                else:
                    break
            break
        return True