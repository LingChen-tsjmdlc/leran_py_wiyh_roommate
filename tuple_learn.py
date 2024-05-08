# ---元组----

# 1，定义

tupleA=(1,2,3,4,5)
tupleB=(1,) #只有一个元素的时候后面要加逗号
print(tupleA)

# 2，索引

print(tupleA[0])
print(tupleA[1])
print(tupleA[2])
print(tupleA[3])
print(tupleA[4])

# 3，切片

print(tupleA[1:3])
print(tupleA[1:])
print(tupleA[:3])
print(tupleA[:])
print(tupleA[-1])

# 4，遍历

for i in tupleA:
    print(i)