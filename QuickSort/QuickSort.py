#quick sort~~~
def quicksort(que,lo,hi): #[lo,hi)
    if hi-lo<2:
        return
    pivot=partation(que,lo,hi-1)
    quicksort(que,lo,pivot)
    quicksort(que,pivot+1,hi)

def partation(que,lo,hi):#[lo,hi)
    pivot=que[lo]
    while lo<hi:
        while lo<hi:
            if pivot<que[hi]:
                hi=hi-1
            else:
                que[lo]=que[hi]
                lo=lo+1
                break
        while lo<hi:
            if que[lo]<pivot:
                lo=lo+1
            else:
                que[hi]=que[lo]
                hi=hi-1
                break
    #assert:lo=hi
    que[lo]=pivot
    return lo

q=[1,9,2,6,4,7,2]
quicksort(q,0,len(q))
print(q)