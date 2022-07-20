from typing import List


class QuikSort:
    def divide(self, arr: List[int], start: int, end: int):
        if start >= end: return
        pivot, left = end, start
        for i in range(start, end):
            if arr[i] < arr[pivot]:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        arr[left], arr[pivot] = arr[pivot], arr[left]
        self.divide(arr, start, left - 1)
        self.divide(arr, left + 1, end)
        return left

    def sort(self, arr: List[int]) -> None:
        self.divide(arr, 0, len(arr) - 1)


class MergeSort:
    def _merge(self, l1: List[int], l2: List[int]) -> List[int]:
        i = j = 0
        ret = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                ret.append(l1[i])
                i += 1
            else:
                ret.append(l2[j])
                j += 1
        while i < len(l1):
            ret.append(l1[i])
            i += 1
        while j < len(l2):
            ret.append(l2[j])
            j += 1
        return ret

    def _sort(self, arr: List[int], start, end: int) -> List[int]:
        if start >= end - 1: return [arr[start]]
        mid = (end + start) >> 1
        l1 = self._sort(arr, start, mid)
        l2 = self._sort(arr, mid, end)
        return self._merge(l1, l2)

    def sort(self, arr: List[int]) -> List[int]:
        return self._sort(arr, 0, len(arr))
