""" ---字符串相关操作题目---"""
# 1,接受一个字符串和一个整数 n 作为参数，将字符串分割为长度为 n 的子串，并返回一个包含这些子串的列表。

# 2,接受一个字符串名字叫songlistId,当用户输入包含空格时,将其输出为没有空格的样式

# 3,接受一个字符串和一个字符串列表作为参数，将列表中的所有单词都替换为字符串中第一个单词的长度，并返回替换后的字符串。
#   例如，如果字符串是 "This is a test string"，字符串列表是 ["apple", "banana", "orange"]，则应该返回 "4 4 4 4 4"。

# 4,[!列表题!]π/4=1-1/3+1/5-1/7+...
#   利用循环结构使用上面的式子计算最后一项分母为59、999、9999、99999、999999时，π的值，并按照指定格式输出结果。
#   例如： 分母为59时，输出:算到1/59时，π=3.10826856669894713292;最后把所有结果用逗号拼接起来.

# 5,接受一个字符串和一个整数列表作为参数，整数列表表示字符串中需要删除的字符的索引。
#   应该返回一个新的字符串，其中删除了指定索引处的字符。

# stringA="Welcome to my world"
# n=3
# for i in stringA:
#     print(i)

print("\n第一题")



# print("\n第二题")
# songlistId=input("输入一个元素")
# print(songlistId.strip())

print("\n第三题")

stringB = "This is a test string"
# 使用 split 方法拆分成单词列表
word_list = stringB.split(" ", 4)
# 获取单词列表的第一个元素
theFirstWord = word_list[0]
print("stringB的第一个单词：", theFirstWord)
seeTheFirstWordLength=len(theFirstWord)
print(seeTheFirstWordLength)

listFruit = ["apple", "banana", "orange"]
listFruitLength = len(listFruit)
print(listFruitLength)

result = (str(seeTheFirstWordLength) + ' ') * listFruitLength
print(result)






# print("\n第四题")


# x=0
# for i in [59,999,9999,99999,999999]:
#     n=(i+1)/2
#     print(n)
#     for m in range(x+1):
#         print(m)



print("\n第五题")
stringC="Welcome to my world!"
listA=[4]

for i in listA:
    stringC[i]
    print(stringC[i])
    newStringC=stringC.split(stringC[i],1)

    merged_string = ''.join(newStringC)
    print(merged_string)




