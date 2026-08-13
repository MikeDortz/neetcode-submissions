class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        if len(num_set) != len(nums):
            return True
        return False

def main(nums):
    solution = Solution()
    return solution.hasDuplicate(nums)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(eval(sys.argv[1]))
    main(sys.argv[0])