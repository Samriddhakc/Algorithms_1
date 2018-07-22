def bubble_sort(random_list):
    length=len(random_list)
    A=random_list
    for i in range(length):
        for j in reversed(range(i,length,1)):
            if A[j]<A[j-1]:
                swap=A[j-1]
                A[j-1]=A[j]
                A[j]=swap

def main():
   list_1=[1,2,3,4]
   bubble_sort(list_1)
   list_2=[4,3,2,1]
   bubble_sort(list_2)
   
main()
