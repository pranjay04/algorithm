def binarysearch_rec(array, key):
    l = 0
    h = len(array) - 1

    def search(array, l, h, key):
        if l > h:
            return False
        mid = (l + h)//2
        if array[mid] == key:
            return mid
        if key < array[mid]:
            h = mid - 1
        else:
            l = mid + 1
        return search(array, l, h, key)



    return search(array, l, h, key)
