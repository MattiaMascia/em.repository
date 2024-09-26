numeri = [3, 1, 4, 2, 5]
print(len(numeri)) # Output: 5
numeri.append(6)
print(numeri) # Output: [3, 1, 4, 2, 5, 6]
numeri.insert(2, 10)
print(numeri) # Output: [3, 1, 10, 4, 2, 5, 6]
numeri.remove(4)
print(numeri) # Output: [3, 1, 10, 2, 5, 6]
numeri.sort()
print(numeri) # Output: [1, 2, 3, 5, 6, 10]