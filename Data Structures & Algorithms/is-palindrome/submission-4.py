class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_list = [i.lower() for i in s if i!=' ' and i.isalnum()]

        left_pointer = 0
        right_pointer = len(s_list) - 1

        if len(s_list) < 2:
            return True

        while left_pointer <= right_pointer:
            if s_list[left_pointer] != s_list[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True
        