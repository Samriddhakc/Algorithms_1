from bubble_sort import *
from merge_sort import *
from insertion_sort import *
from merge_sort_without_sentinel import *
import time
import random
def main():
    list_1=random.sample(range(200000000),100000)
    t_1=time.time()
    bubble_sort(list_1)
    t_2=time.time()
    print("bubble_sort_took",t_2-t_1)
    t_1=time.time()
    merge_sort(list_1,0,3)
    t_2=time.time()
    print("merge_sort_took",t_2-t_1)
    t_1=time.time()
    merge_sort_without(list_1,0,3)
    t_2=time.time()
    print("merge_sort_without_sentinel_took",t_2-t_1)
    t_1=time.time()
    insertion_sort(list_1)
    t_2=time.time()
    print("insertion_sort",t_2-t_1)
if __name__=="__main__":
    main()
