list = [2,5,9,14,26,85]
n = 26
pos = -1
def binary_search(list,n):
    
    l = 0
    u = len(list)-1
    
    while l<=u:
        mid = (u+l)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return pos
        else:
            if list[mid] < n:
                l = mid
            elif list[mid] > n:
                u = mid
val = binary_search(list,n)
print(val)