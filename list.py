listA = ["P","y","t","h","o","n"]
listB=[1,50,15,36,48,116,6463,13,46,0,436]
listC=[1,50,15,36,48,16,643,13,46,0,436,444,666]
# print(listA[3])             #列表名[索引值]=>索引所在的那个元素
# print(len(listA))           #len(列表名)=>列表的长度
# print(listA.count("P"))     #字符串/变量.count(某个元素)=>统计 字符串/变量里面 某个元素的 个数
# print(listA.index("h"))     #字符串/变量.index(某个元素)=>查询 字符串/变量里面 某个元素的 索引
                              #且只会返回第一个搜索到的
#---添加---

# 1，insert
listA.insert(1,"1")
print(listA)

#2，append
listA.append("111")             #列表.append("元素")=>在列表的后面添加一个元素
# print(listA)

#3，extend
listA.extend(["2","3"])         #列表.append(["元素","元素",...])=>在列表的后面添加一个或者多个元素
# print(listA)



#---删除---
#1，用索引去删除
del listA[2]
# print(listA)        #['P', 'y', 'h', 'o', 'n', '111', '2', '3']

# 2，删除连续的
del listA[3:5]      #数学表示：[3,5)
# print(listA)        #['P', 'y', 'h', '111', '2', '3']

# 3，用索引删除
listB.pop(2)        #列表.pop(索引)=>删除索引所在的元素，等同于listA[2]
# print(listB)        #[1, 50, 36, 48, 116, 6463, 13, 46, 0, 436]

# 4，删除已知的元素
listA.remove("111") #列表.remove(元素)=>删除括号中的元素
# print(listA)        #['P', 'y', 'h', '2', '3']

# 5，删除列表中所有的元素
# listB.clear()       #列表.clear()=>删除列表中所有的元素
# print(listB)        #[]


#---排序---
# 1，升序排序
listB.sort()
print(listB)

#2,降序
listB.sort(reverse=True)
print(listB)

# 3,反转
listC.reverse()
print(listC)

#!!!-----遍历-----!!!
for name in listA:
    print(name)