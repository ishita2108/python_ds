#creating
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)

print("-----------------------------------------------------")

#accessing
Days={"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}
for d in Days:
	print(d)

print("-----------------------------------------------------")

#adding
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Days.add("Sun")
print(Days)

print("-----------------------------------------------------")

#removing
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Days.remove("Sun")
Days.discard("Mon")
print(Days)

print("-----------------------------------------------------")

#union
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)

print("-----------------------------------------------------")

#intersection
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)

print("-----------------------------------------------------")

#difference
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)

print("-----------------------------------------------------")

#compare
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)