L = [64, 34, 25, 12, 22, 11, 90]
print("Liste avant tri :", L)

nombre = 0
for element in L:
        nombre += 1

for i in range(nombre):
    for j in range(0, nombre-i-1):
        if L[j] > L[j+1]:
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp

print("Liste après tri :", L)