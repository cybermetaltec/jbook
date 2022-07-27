class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        nums, flag, ret = [], None, 0
        Max, Min = (1 << 31) - 1, -1 << 31
        for char in s:
            if 48 <= (asi := ord(char)) <= 57:
                nums.append(asi - 48)
            elif char in ("-", "+") and not nums and flag is None:
                flag = -1 if char == "-" else 1
            else:
                break
        for i, n in enumerate(nums):
            ret += n * (10 ** (len(nums) - i - 1)) if n or ret else 0
        if flag: ret *= flag
        return max(min(ret, Max), Min)

