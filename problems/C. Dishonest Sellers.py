n,k=map(int,input().split(" "))
lst1=list(map(int,input().split(" ")))
lst2=list(map(int,input().split(" ")))
d=sorted(a-b for a,b in zip(lst2,lst1) if(a-b<0))
print("{}".format(sum(lst1)+sum(d[:n-k])))