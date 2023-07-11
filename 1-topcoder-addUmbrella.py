'''
Every possible umbrella position has to be checked i.e. 
for a position to be considered a proper umbrella position 
there must not be a Bee on its way horizontally and vertically.
But doing this would take time. Therefore a memory has to be used
to save all the Bees that are below a certain position, the number 
of free spots to left and right, whether the handle can touch the ground.

(belowBees, freeLeft, freeRight, isTouchingGround). 

This is done to every position and it will take O(n*m) time. 
Also checking and tracking the largest number of bees protected
will take O(n*m*m) time, n being the rows and m being the columns.
Time complexity: O(n*m*m)
Space complexity: O(n*m)
'''
from typing import List
def solve(s: List[str]) -> int:
    memo = []
    for i in range(len(s)):
        memo.append([[0, s[i][0] == '.', 0, False]])
        for j in range(1, len(s[i])):
            freeLeft = 0 if s[i][j] == 'B' else memo[i][j-1][1] + 1
            memo[-1].append([0, freeLeft, 0, False])

    for i in range(len(memo)-2, -1, -1):
        memo[i][-1][2] = s[i][-1] == '.'
        memo[i][-1][0] = (s[i][-1] == 'B') + memo[i+1][-1][0]
        for j in range(len(s[i])-2, -1, -1):
            freeRight = 0 if s[i][j] == 'B' else memo[i][j+1][2] + 1
            memo[i][j][0] = memo[i+1][j][0] + (s[i][j] == 'B')
            memo[i][j][2] = freeRight
            memo[i][j][3] = memo[i+1][j][0] == 0 and s[i][j] == '.' and i < len(s)-2

    res = 0
    for i in range(len(s)-2):
        for j in range(1, len(s[i])-1):
            if memo[i][j][3]:
                width = min(memo[i][j-1][1], memo[i][j+1][2])
                shaded = 0
                for k in range(1, width+1):
                    shaded += memo[i][j+k][0] + memo[i][j-k][0]
                res = max(res, shaded)
    
    return res
