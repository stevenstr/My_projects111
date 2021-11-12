n = 5

matrix5 = [[0 for j in range(n)] for i in range(n)]
print("Sixe is:", n,"x", n)
print(matrix5)

print()
print(matrix5[0])
print(matrix5[1])
print(matrix5[2])
print(matrix5[3])
print(matrix5[4])
print()

for i in range(n):
    print(matrix5[i])

print()
matrix5[0][0] = 99
for i in range(n):
    print(matrix5[i])
