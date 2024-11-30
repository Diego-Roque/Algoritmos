def min_steps_to_friend(x):

    steps = x // 5
    if x % 5 != 0:
        steps += 1
    return steps


x = int(input().strip())
print(min_steps_to_friend(x))
