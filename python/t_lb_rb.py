def lower_bound(seq, x):
    l = 0
    r = len(seq)
    while l < r:
        mid = (l + r) // 2
        if seq[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return l if seq[l] == x else -1


def upper_bound(seq, x):
    l = 0
    r = len(seq)
    while l < r:
        mid = (l + r) // 2
        if seq[mid] > x:
            r = mid
        else:
            l = mid + 1
    return l if (l > 0 and seq[l - 1] == x) else -1


seq = [0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9]
l = lower_bound(seq, -1)
r = upper_bound(seq, 8)
print(l, r)
