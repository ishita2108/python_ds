list = [85,45,96,75,23,1,20,23,656,91]

def shell_sort(list):
    size = len(list)
    gap = size//2
    while gap > 0:
        for i in range(gap,size):
            anchor = list[i]
            j = i
            while j >= gap and list[j-gap] > anchor:
                list[j] = list[j-gap]
                j -= gap
            list[j] = anchor
        gap = gap//2


    return list
val = shell_sort(list)
print(val)