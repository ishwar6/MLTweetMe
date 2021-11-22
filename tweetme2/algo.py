items = [2, 3, 5, 6, 7, 11, 33, 44, 56, 76, 88, 98, 101]


def binary_search(items, x, low, high):

    print("running for", low, high, items)
    if high > low:
        mid = (low + high)//2
        print("MIID", mid)

        if items[mid] == x:
            return mid

        elif items[mid] > x:
            return binary_search(items, x, low, mid-1)
        else:
            return binary_search(items, x, mid+1, high)
    else:
        print("NOT FOUND")


#a = binary_search(items, 991, 0, len(items))
# print(a)


def binary_search_i(items, x):

    low, high = 0, len(items)-1

    while high > low:

        mid = (low+high)//2
        print("running for", low, high, mid)
        if items[mid] == x:
            return mid
        elif items[mid] > x:
            high = mid-1
        else:
            low = mid+1
        print("NEXT running for", low, high, mid)


print(binary_search_i(items, 6))
