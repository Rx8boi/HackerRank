if __name__ == '__main__':
    n = int(input())
    
    arr=[]
    i=0
    while i < n:
        arr.append(i**2)
        i+=1
        
    for x in arr:
        print(x)
