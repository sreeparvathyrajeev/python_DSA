from math import gcd
from functools import reduce

def get_ans(n, a, p, q, queries):
    yes_count = 0

    for i, j in queries:
        # update (queries are 1-indexed)
        a[i - 1] = j

        # collect elements divisible by p
        b = []
        for x in a:
            if x % p == 0:
                b.append(x // p)

        # must be non-empty
        if not b:
            continue

        # gcd of all candidates
        g = reduce(gcd, b)

        # conditions for GOOD subsequence
        if g == 1 and len(b) < n:
            yes_count += 1

    return yes_count
if __name__=="__main__":
    n=int(input())
    a=[int(input()) for _ in range(n)]
    p=int(input())
    q=int(input())
    col=int(input())
    queries=[tuple(map(int, input().split())) for _ in range(q)]
    print(get_ans(n, a, p, q, queries))