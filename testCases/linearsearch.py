def search(arr: list, x: int):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
