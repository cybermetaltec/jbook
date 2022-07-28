class Solution:
    def _reverse(self, arr, start, end, k) -> None:
        if end - start > k: end = start + k
        end = end - 1
        while start < end:
            if arr[start] != arr[end]: arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        i = 1
        while i * 2 * k <= len(s):
            self._reverse(s, (i - 1) * 2 * k, i * 2 * k, k)
            i += 1
        if (i - 1) * 2 * k < len(s) < i * 2 * k:
            self._reverse(s, (i - 1) * 2 * k, len(s), k)
        return "".join(s)
