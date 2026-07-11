class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i])) + "#" + strs[i]

        return s


    def decode(self, s: str) -> List[str]:
        decodedlst = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            decodedlst.append(s[j+1:j+1+length])
            i = j + 1 + length

        return decodedlst

