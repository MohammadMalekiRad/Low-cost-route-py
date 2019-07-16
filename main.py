from random import randint as rn
from math import sqrt as radical

start_point_input = [int(x) for x in input("Enter start point, like this x y: ").split()]  # exp: [1, 1]
end_point_input = [int(x) for x in input("Enter end point: like this x y: ").split()]  # exp: [5, 5]
cost_input = int(input("Enter cost: "))
costs = []


# this function give me a mini path, for example
# Depending on the way forward to the destination,
# we return the coordinates that are customary
def mini_path(top, right):
    # top and right
    if top_and_right(top, right) == (True, True):
        return [
            # x+1, y
            [top[0] + 1, top[1]],
            # x+1, y+1
            [top[0] + 1, top[1] + 1],
            # x, y+1
            [top[0], top[1] + 1]
        ]

    # bottom and left
    if top_and_right(top, right) == (False, False):
        return [
            # x-1, y
            [top[0] - 1, top[1]],
            # x-1, y-1
            [top[0] - 1, top[1] - 1],
            # x, y - 1
            [top[0], top[1] - 1]
        ]

    # bottom and right
    if top_and_right(top, right) == (False, True):
        return [
            # x+1, y
            [top[0] + 1, top[1]],
            # x+1, y-1
            [top[0] + 1, top[1] - 1],
            # x, y-1
            [top[0], top[1] - 1]
        ]

    # top and left
    if top_and_right(top, right) == (True, False):
        return [
            # x-1, y
            [top[0] - 1, top[1]],
            # x-1, y-1
            [top[0] - 1, top[1] + 1],
            # x, y-1
            [top[0], top[1] + 1]
        ]


# This function is to determine the direction of progress in the path.
def top_and_right(first_point, end_point):
    is_right = False
    is_top = False

    # x end point > x end point => move right
    if end_point[0] > first_point[0]:
        is_right = True

    # y end point > y end point => move top
    if end_point[1] > first_point[1]:
        is_top = True

    return is_top, is_right


# *********************************************************** #
# Loop to repeat 5 times
for i in range(5):

    start = start_point_input
    end = end_point_input
    cost_bfr = cost_input
    while True:

        bfr = mini_path(start, end)
        rnd = rn(0, 2)
        one_choose = bfr[rnd]

        # print(rnd, one_choose, bfr)

        if rnd == 1:
            cost_bfr *= radical(2)
        else:
            cost_bfr *= 1

        # print(rnd)

        if one_choose == end_point_input:
            print("Cost: ", cost_bfr)
            costs.append(cost_bfr)
            break

        start = one_choose

print(min(costs))
