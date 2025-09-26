def casechange(F,L):
    F=F.lower()
    L=L.upper()
    return F+" "+L
if __name__=="__main__":
    F=input()
    L=input()
    print(casechange(F,L))