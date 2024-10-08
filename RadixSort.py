def Radixsort(arr):
    maxv=max(arr)
    pos=1
    while maxv//pos>0:
        Countsort(arr,pos)
        pos=pos*10

def Countsort(arr,pos):
    n=len(arr)
    count=[0]*10
    output=[0]*n
    for i in arr:
        index=(i//pos)%10
        count[index]+=1
    for i in range(1,10):
        count[i]=count[i]+count[i-1]
    for num in reversed(arr):
        index=((num//pos)%10)
        output[count[index]-1]=num
        count[index]=count[index]-1
    for i in range(n):
        arr[i]=output[i]

def printarray(arr):
    for i in arr:
        print(i,end=" ")

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
Radixsort(arr)
printarray(arr)

