class Solution:
    def valid(self, asi: int) -> bool:
        if 65 <= asi <= 90 or 97 <= asi <= 122: return True
        return False

    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            asi_l, asi_r = ord(arr[l]), ord(arr[r])
            valid = [self.valid(asi_l), self.valid(asi_r)]
            if not valid[0]:
                l += 1
                continue
            if not valid[1]:
                r -= 1
                continue

            if valid[0] and valid[1] and asi_r != asi_l:
                arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return "".join(arr)


print(Solution().reverseOnlyLetters("ab-cd"))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
