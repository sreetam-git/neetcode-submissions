class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None

        result = {}
        for word in strs:
            key = "".join(sorted(word))
            result[key] = result.get(key, [])
            result[key].append(word)

        return list(result.values())