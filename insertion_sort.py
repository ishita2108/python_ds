list = [85,45,96,75,23,1,20,23,656,91]

def insertion_sort(list):
    for i in range(1,len(list)):
        value = list[i]
        j = i-1
        while j>=0:
            if value < list[j]:
                list[j+1] = list[j]
                list[j] = value
                j = j-1
            else:
                break
    return list
val = insertion_sort(list)
print(val)