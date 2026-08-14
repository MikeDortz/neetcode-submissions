class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for word in strs:
            sort_str = sorted(word)
            sort_word = str(sort_str)
            if ana.get(sort_word):
                ana[sort_word].append(word)
            else:
                ana[sort_word] = [word]
        
        return list(ana.values())