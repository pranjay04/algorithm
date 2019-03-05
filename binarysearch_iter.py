def binarysearch_iter(array,key):
    l = 0
    h = len(array)-1
    while(l<=h):
        mid = (l + h)//2
        if key == array[mid]:
            return mid
        if key < array[mid]:
            h = mid-1
            pass
        else:
            l = mid+1
    return False
