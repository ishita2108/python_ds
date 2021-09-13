list = [21,5,4,89,67,26,55,32]
n = 21

def linear_search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return i
    print("Not Found")
val = linear_search(list,n)
print(val)
