def charoccur(S,N,C):
    count = 0
    for char in S:
        if char == C:
            count += 1
    return count
if __name__ == "__main__":
    S=input()
    N=input()
    C=input()
    print(charoccur(S,N,C))