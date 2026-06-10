# Given a string S and a character C, find the number of occurrences of C in S.
def charoccur(S,C):
    count = 0
    for char in S:
        if char == C:
            count += 1
    return count
if __name__ == "__main__":
    S=input()   
    C=input()
    print(charoccur(S,C))
