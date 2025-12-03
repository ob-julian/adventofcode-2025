x = range(10)
print(len(x))
for iterator, number in enumerate(x):
    print("remaining numbers: ", len(x) - iterator- 1)