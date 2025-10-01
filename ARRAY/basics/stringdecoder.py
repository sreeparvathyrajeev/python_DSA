def decode(string):
    lst1=string.split('0')
    result=''
    for i in lst1:
        temp=chr(len(i)+64)
        result +=temp
    return result
if __name__ == '__main__':
    string=input()
    print(decode(string))