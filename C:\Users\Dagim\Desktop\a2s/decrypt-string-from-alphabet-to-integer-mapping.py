class Solution(object):
    def freqAlphabets(self, s):
        result = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = int(s[i - 2: i])
                result.append(chr(num + 96))  # Map to lowercase letter using ASCII code
                i -= 3
            else:
                num = int(s[i])
                result.append(chr(num + 96))  # Map to lowercase letter using ASCII code
                i -= 1
        return ''.join(result[::-1])  # Reverse the result and convert to string

