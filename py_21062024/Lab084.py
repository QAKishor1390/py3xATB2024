# for loop in set

set1 = set(["TheTestingAcademy", "For", "TheThestingAcademy"])
print(len(set1))

for i in set1:
    print(i)

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(set1)
print(len(set1))
set1.remove(5)
print(set1)

set1.add(100)
print(set1)

set1.pop()
print(set1)
