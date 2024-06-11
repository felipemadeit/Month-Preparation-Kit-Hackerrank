def plus_minus (n: int, arr: list):

    negative = 0
    positive = 0
    zeroes = 0

    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else :
            zeroes += 1

    positive_ratio = round(positive / n, 6)
    negative_ratio = round(negative / n, 6)
    zeroes_ratio = round(zeroes / n, 6)

    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zeroes_ratio:.6f}")



plus_minus(int(input()), arr = [int(x) for x in input().split()])