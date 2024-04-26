#题目1：
# 新建一个列表，让用户输入信息来组成一个完整的列表。
# 列表格式：["歌曲名","歌手名","风格","语言","sc","备注"]

#题目2：
# 删除题目一中的备注这个元素，然后添加新的一个备注

#题目3：
# 将列表[22,33,1,30,15,36,48,55,643,13,46,0,436,444,666]按照由大到小排序

#题目4：
#删除题目三列表中所有的元素，让用户重新添加5个新的元素

#题目5：
#遍历题目2中的列表，然后用逗号组成一行（歌曲名,歌手名,风格,语言,sc,备注）

ListA=[]
ListB=[22,33,1,30,15,36,48,55,643,13,46,0,436,444,666]


#题目1
print("题目1：")
ListA.append(input("输入歌曲名"))
ListA.append(input("输入歌手名"))
ListA.append(input("输入风格"))
ListA.append(input("输入sc"))
ListA.append(input("输入语言"))
ListA.append(input("输入备注"))
print("ListA:",ListA)

#题目2
print("题目2：")
del ListA[5]
ListA.append(input("输入一个新的备注"))
print("ListA:",ListA)

#题目3
print("题目3：")
ListB.sort(reverse=True)
print("ListB:",ListB)

#题目4
print("题目4：")
ListB.clear()
print("ListB:",ListB)
ListB.extend([input("输入第一个新的元素"),input("输入第二个新的元素"),input("输入第三个新的元素"),input("输入第四个新的元素"),input("输入第五个新的元素"),])
print("ListB:",ListB)

#题目5
print("题目5：")
ListC=[str(message) for message in ListA]
print("ListC:",ListC)
for message in ListA:
    print(message,end=",")