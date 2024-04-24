import math

# 变量名=值
# 使用变量，要先定义，再使用
a=0  #a:变量名,1:值
b=False
q="0"

# 类型(数字)
# 1，int     整数：1，50，-100
# 2，float   浮点数：1.5，3.14159267（long：3.16465465465484534...）
# 3,bool     布尔类型：True(真!=0),False（假=0）

# 类型(字符类型)
# 1，string  字符串：代表的是一串文字
# 2，list    列表:[1,2,3,4,5,6,7]
listA = ["P","y","t","h","h","h"]
# print(listA[3])             #列表名[索引值]=>索引所在的那个元素
# print(len(listA))           #len(列表名)=>列表的长度
# print(listA.count("P"))     #字符串/变量.count(某个元素)=>查询 字符串/变量里面 某个元素的个数
# print(listA.index("h"))     #字符串/变量.index(某个元素)=>查询 字符串/变量里面 某个元素的索引
                            #且只会返回第一个搜索到的
# 3，元组
# 4，字典

# ----------题目----------
listId=9537359452
buid=385641614
url="https://music.163.com/playlist?id=7538493305&userid=1478422750"    # 变量名=值
genre=["Ending","Sparse_piano_notes","pounding_drums","gentle_vocals"]

#1，把上述的listId，buid，url变成一个列表，并输出这个数组的长度
#2，找到genre列表中的pounding_drums在第几个索引位置
#3，查找genre列表中gentle_vocals是多少索引

listB=[listId,buid,url,genre]
print((len(listB)))

print(genre.index("pounding_drums"))

print(genre.count("gentle_vocals"))

# NaN = Not a Number  #不是个数
# null                #空
# error               #错误
# warning             #警告
#aslpdka
#lkalaka=kdkkd