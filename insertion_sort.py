def insertion_sort(list):
    length=len(list)
    for i in range(1,length,1):
        j=i-1
        key=list[i]
        while key<=list[j] and j>=0:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=key
    return list

def main():
   print(insertion_sort([1,2,3,4]))
   print(insertion_sort([4,3,2,1]))
   print(insertion_sort([100,-10,200,20]))
main()
