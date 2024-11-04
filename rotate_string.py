# Question :
# https://leetcode.com/problems/rotate-string/
# Learning/Approach to check if a string can be formed by rotating other we can add string side by side and check if we can goal is substring of str+str

def rotateString(self, s: str, goal: str) -> bool:
    if len(goal) != len(s):
        return False
    g = goal + goal
    if s in g:
        return True
    else:
        return False