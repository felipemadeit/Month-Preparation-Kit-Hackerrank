def mini_max (arr: list):

    arr.sort()

    min_arr = arr[:-1]
    max_arr = arr[1:]


    print(f"{sum(min_arr)} {sum(max_arr)}")


mini_max(arr = [int(x) for x in input().split()])