#Author : 5hifaT

#Github        : https://github.com/jspw

#Gists         : https://gist.github.com/jspw

#linkedin      : https://www.linkedin.com/in/mehedi-hasan-shifat-2b10a4172/

#Stackoverflow : https://stackoverflow.com/story/jspw 

#Dev community : https://dev.to/mhshifat




def binary_search(ar, value):
    start = 0
    end = len(ar)-1
    while(start <= end):
        mid = (start+end)//2
#        print("start : {},end : {},mid {}".format(start, end, mid), end=" ")
        if(ar[mid] == value):
            return mid
        if(ar[mid] > value):
            end = mid-1
        else:
            start = mid+1
    return -1


def main():
    l = input()
    print(l)
    ans=[]
    target = int(input())
    for i in range (1,len(l),2):
        for j in range(i+2,len(l),2):
            print(l[i])
            print(l[j])
            if(int(l[i])+int(l[j])==target):
                ans.append(i)
                ans.append(j)
    print(ans)

if __name__ == "__main__":
    main()
