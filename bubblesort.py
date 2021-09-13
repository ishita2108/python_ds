list = [85,45,96,75,23,1,20,23,656,91]

def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] >  list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
val = bubble_sort(list)
print(val)
