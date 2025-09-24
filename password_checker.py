def password_checker(password):
    n= len(password)
    if n<4:
        return "weak"
    if password[0].isdigit():
        return "weak"
    cap=0
    nu=0
    for i in range(n):
        if password[i]==" " or password[i]=="/":
            return "weak"
        if "A"<=password[i]<="Z":
            cap+=1
        elif password[i].isdigit():
            nu+=1
        else:
            pass
    if cap>=1 and nu>=1:
        return "strong"
    else:
        return "weak"   
    
