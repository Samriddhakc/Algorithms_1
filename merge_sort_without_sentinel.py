from __future__ import division
import math

def merge(main_list,lower_bound,mid_point,upper_bound):
    first_half=main_list[lower_bound:mid_point]     
    second_half=main_list[mid_point:upper_bound+1]
    #first_half.append(1000000)
    #second_half.append(1000000)
    i=0
    j=0
    counter=0
    for running_index in range(lower_bound,upper_bound+1,1):       
        counter=running_index
        if(i<len(first_half) and j<len(second_half)):
            if first_half[i]<=second_half[j]:
                main_list[running_index]=first_half[i]
                i=i+1
            else:
                main_list[running_index]=second_half[j]
                j=j+1
        else: 
            if(i==len(first_half)):
                first=True 
            else:
                first=False
            break
    if first==True:
        main_list[counter:upper_bound+1]=second_half[j:]       
    elif first==False:
        main_list[counter:upper_bound+1]=first_half[i:]

def merge_sort_without(main_list,lower_bound,upper_bound):
    if lower_bound<upper_bound:
        mid_point=int(math.ceil((lower_bound+upper_bound)/2))
        merge_sort_without(main_list,lower_bound,mid_point-1)
        merge_sort_without(main_list,mid_point,upper_bound)
        merge(main_list,lower_bound,mid_point,upper_bound)


def main(): 
    list_2=[4,-1]
    list_3=[1,2,3,4,-100,-200,20]
    list_4=[0]
    list_5=[1/3,2/3,100,0,-100/3,500,600]
    merge_sort_without(list_2,0,1)
    merge_sort_without(list_3,0,6)
    merge_sort_without(list_4,0,0)
    merge_sort_without(list_5,0,6)
main()






