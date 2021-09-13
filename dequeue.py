import collections

DoubleEnded = collections.deque(["Mon","Tue","Wed"])

DoubleEnded.append("Thu")

print ("Appended at right - ")
print (DoubleEnded)

DoubleEnded.appendleft("Sun")

print ("Appended at left is - ")
print (DoubleEnded)

DoubleEnded.pop()

print ("Deleting from right - ")
print (DoubleEnded)

print ("Deleting from left - ")
print (DoubleEnded.popleft())
print(DoubleEnded)