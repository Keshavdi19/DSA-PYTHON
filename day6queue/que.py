class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0  # slow pointer (last unique element का index)
        for j in range(1, len(nums)):  # fast pointer पूरे array पर चलेगा
            if nums[j] != nums[i]:     # नया unique element मिला
                i += 1                 # unique index आगे बढ़ाओ
                nums[i] = nums[j]      # उस जगह नया unique रख दो

        return i + 1   # unique elements की count (क्योंकि i index है)


# ---------------- Main Code ----------------
if __name__ == "__main__":
    # Example Input
    nums = [0,0,1,1,1,2,2,3,3,4]

    # Object बनाना
    sol = Solution()
    k = sol.removeDuplicates(nums)

    # Output
    print("Number of unique elements:", k)
    print("Array after removing duplicates:", nums[:k])
