def mysquare(x):
    return x**2

num = [1, 2, 3, 4, 5]
sq = []

for i in num:
    sq.append(mysquare(i))

print(sq)

#list(map(lambda x : x**2,num))