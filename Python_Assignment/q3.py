# 3. Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#     An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#     Constraints:

#         - 1 <= strs.length <= 104

#         - 0 <= strs[i].length <= 100

#         - strs[i] consists of lowercase English letters.

#     Example 1:

#         - Input: strs = ["eat","tea","tan","ate","nat","bat"]

#         - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#     Example 2:

#         - Input: strs = [""]

#         - Output: [[""]]

#     Example 3:

#         - Input: strs = ["a"]

#         - Output: [["a"]]
def anagram(str):
    result = []
    visited = [False] * len(str)
    
    for i in range(len(str)):
        if not visited[i]:
            store = []
            temp1 = list(str[i])
            temp1.sort()  # str[i].split().sort()

            for j in range(len(str)):
                if not visited[j]:
                    temp2 = list(str[j])
                    temp2.sort()

                    if temp1 == temp2:
                        store.append(str[j])
                        visited[j] = True
        
            result.append(store)
    
    return result
            
strs = ["eat","tea","tan","ate","nat","bat"]
anagram_li = anagram(strs)
anagram_li.sort()
print(anagram_li)


# strs = [""]

# strs = ["a"]