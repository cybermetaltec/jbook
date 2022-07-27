from typing import List


# class Solution:
#     def _lower(self, s_list: List[str]) -> List[str]:
#         if len(s_list) == 1:
#             ascii = ord(s_list[0])
#             return [chr(97 + ascii - 65)] if 65 <= ascii <= 90 else s_list
#         mid = len(s_list) >> 1
#         left = self._lower(s_list[:mid])
#         right = self._lower(s_list[mid:])
#         ret = left + right
#         return ret
#
#     def toLowerCase(self, s: str) -> str:
#         arr = self._lower(list(s))
#         return "".join(arr)

class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([chr(asi + 32) if 65 <= (asi := ord(c)) <= 90 else c for c in s])
