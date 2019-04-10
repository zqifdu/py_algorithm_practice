"""
纸牌游戏，
纸牌上面有值，比如说 100， 1， -1， 2， 200， 1.
然后两个人轮流拿，直到拿完。
但是每次只能拿从左边数起的前三个，
但是如果你要拿第三个，就必须前两个都拿了，你要拿第二个，就必须第一个也拿了，
大家都最优策略，问最后第一个人能拿多少分。
"""


def minimax(cards, start_player, start, play1_point):
    if start == len(cards):
        return play1_point

    if start_player == 1:  # player 1 starts to play
        max_point = float('-inf')

        for i in range(3):
            if i + start == len(cards):
                return max_point
            play1_point += cards[start + i]
            total_point = minimax(cards, 2, start + i + 1, play1_point)
            if total_point > max_point:
                max_point = total_point

        return max_point
    else:   # player 2 starts to play
        min_point = float('inf')
        for i in range(3):
            if i + start == len(cards):
                return min_point
            total_point = minimax(cards, 1, start + i + 1, play1_point)
            if total_point < min_point:
                min_point = total_point

        return min_point

def max_play1_point(cards):
    return minimax(cards, 1, 0, 0)

cards = [0, 1, 1, 1, 5]

print(max_play1_point(cards))