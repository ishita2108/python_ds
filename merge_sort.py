list = [85,45,96,75,23,1,20,23,656,91]

def merge_sort(list):
    if len(list)<=1:
        return list
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_sort_two_list(left,right)

def merge_sort_two_list(a,b):
    sorted_list = []
    len_a = len(a)
    len_b =len(b)
    i=j=0
    while i<len_a and j <len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i = i+1
        else:
            sorted_list.append(b[j])
            j = j+1
    while i<len_a:
        sorted_list.append(a[i])
        i+=1
    while j<len_b:
        sorted_list.append(b[j])
        j+=1
    return sorted_list
val = merge_sort(list)
print(val)