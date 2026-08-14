class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dct = {}
        for num in nums:
            if dct.get(num):
                dct[num] += 1
            else:
                dct[num] = 1
        
        # copied from web on how to sort dictionary based on values
        sort_dct = dict(sorted(dct.items(), key=lambda item: item [1], reverse=True))

        # copied from web on how to return first k keys
        return list(islice(sort_dct, k))

