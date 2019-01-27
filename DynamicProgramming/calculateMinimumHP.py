# leetcode 174:
# https://leetcode.com/problems/dungeon-game/


# Other's solutions
# https://leetcode.com/problems/dungeon-game/discuss/52792/6-lines-Python-8-lines-Ruby
def calculateMinimumHP(dungeon):
    n = len(dungeon[0])
    need = [2**31] * (n-1) + [1]
    for row in dungeon[::-1]:
        for j in range(n)[::-1]:
            need[j] = max(min(need[j:j+2]) - row[j], 1)
    return need[0]


dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5], [0, 0, -40]]
print(calculateMinimumHP(dungeon))