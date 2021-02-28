import heapq

T = int(input())
while T:
    T -= 1
    N = int(input())
    people = input()
    M = int(input())
    genders = input()
    people = [int(x) for x in people]
    heap0 = []
    heap1 = []
    for i, person in enumerate(people, start=1):
        if person == 0:
            heapq.heappush(heap0, i)
        if person == 1:
            heapq.heappush(heap1, i)
    for gender in genders:
        f0 = heap0[0] if heap0 else 0
        f1 = heap1[0] if heap1 else 0
        if gender == 'M':
            ans = 'f1' if f1 else 'f0'
        else:
            ans = 'f0' if f0 else 'f1'
        if ans == 'f1':
            heapq.heappop(heap1)
            print(f1)
        else:
            heapq.heappush(heap1, heapq.heappop(heap0))
            print(f0)
        # print(f1 if ans == 'f1' else f0)
