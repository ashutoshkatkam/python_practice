# Question URL
# https://leetcode.com/problems/ransom-note/description/

# Approach/Learning
# Create a hash map for letters in magazine
# Iterate over ransonNote to check if letter is in hashmap while updating the count of used letters

def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag = {}
    for m in magazine:
        mag[m] = mag.get(m,0) + 1
    # print(mag)
    for r in ransomNote:
        if r not in mag.keys():
            return False
        else:
            mag[r] -= 1
            if mag[r] == 0:
                mag.pop(r)
    return True

print(canConstruct('a','ab'))