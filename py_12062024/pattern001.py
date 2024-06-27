# ows = int(input("Enter the number of rows: "))
#
# for i in range(1, rows + 1):
#   for j in range(i):
#     print("*", end=" ")
#   print()

rows=int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(i,rows + i):
        print(i,end=" ")
    print()






