#creating heap
import heapq
H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

print("---------------------------------------------------------")

#inserting
heapq.heappush(H,8)
print(H)

print("---------------------------------------------------------")

# Remove element from the heap
heapq.heappop(H)
print(H)

print("---------------------------------------------------------")

# Replace an element
heapq.heapreplace(H,6)
print(H)