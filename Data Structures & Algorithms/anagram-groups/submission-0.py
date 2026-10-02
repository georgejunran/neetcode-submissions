class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list) 

        #within the dictionary arrange each set of anagram letter based on which letter combo
        for word in strs:
            count = [0] * 26

            #set count to 0
            for char in word:
                count[ord(char) - ord("a")] += 1

            anagrams[tuple(count)].append(word)

        return list (anagrams.values())