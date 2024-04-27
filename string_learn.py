stringA="hello,world!"  # 在字符串的定义中，双引号和单引号都可以
stringB="114514"
stringC="壹"
stringD="Hello"


""" --- 基本用法 --- """
print("stringA中第五个索引的元素是:",stringA[5])       #可以用索引来获取指定位置的字符串

# for i in stringA:       #for...in...可以遍历字符串
#     print(i)

print("stringA的长度:",len(stringA))     #len(字符串名)=>字符串的长度

print("字符“l”的个数:",stringA.count("l"))#字符串.count(某个字符)=>查询 字符串里面 某个字符的个数

print("字符“l”的索引:",stringA.index("l"))#字符串.index(某个字符)=>查询 字符串里面 某个字符的索引




""" --- 判断字符串类型---  """
# 1，判断是否有空格
print(stringA.isspace())        #stringA.isspace() 判断字符串中是否只包含空格
# 2,判断字符串中至少有一个字符且字符中所有的元素是字母或数字
print(stringA.isalnum())        #stringA.isalnum() 判断字符串中是否只包含字母或数字[is al num===>is all number]
# 3,判断字符串中至少有一个字符,且所有的元素都是字母
print(stringA.isalpha())        #stringA.isalpha() 判断字符串中是否只包含字母
# 4,判断字符串中至少有一个字符,且所有的元素都是数字
print(stringB.isdigit())        #stringA.isdigit() 判断字符串中是否只包含数字
# 5,判断字符串中至少有一个字符,且所有的元素都是全角数字
print(stringB.isdecimal())
# 6,判读字符串中至少有一个字符,且所有的元素都是全角数字和汉字数字
print(stringC.isnumeric())
# 7,判断字符串是否为标题化的多字符串
print(stringD.istitle())
# 8,判断字符串中的 所有 字符是否都是小写字母
print(stringA.islower())
# 9,判断字符串中的 所有 字符是否都是大写字母
print(stringA.isupper())


print("\n --- 字符串的查找和替换 --- ")
""" --- 字符串的查找和替换 --- """
# 1,检查字符串是否以某个字符开头
print(stringA.startswith("h"))
# 2,检查字符串是否以某个字符结尾
print(stringA.endswith("!"))
# 3,检查字符串中是否包含某个字符,从左边开始找
print(stringA.find("l"))#字符串.find(某个字符)=>查询 字符串里面 某个字符的索引
# 4,检查字符串中是否包含某个字符,从右边开始找
print(stringA.rfind("k"))#字符串.rfind(某个字符)=>查询 字符串里面 某个字符的索引
# 5,检查字符串中是否包含某个字符,如果查找的元素没有,会报错
print(stringA.index("l"))#字符串.index(某个字符)=>查询 字符串里面 某个字符的索引
# 6,检查字符串中是否包含某个字符,从右边开始找,如果查找的元素没有,会报错
print(stringA.rindex("l"))#字符串.rindex(某个字符)=>查询 字符串里面 某个字符的索引
# 7,替换
print(stringA.replace("Hello","hello",1))   #replace(老的值,新的值,替换次数)


print("\n --- 字符串的大小写转换 --- ")
""" --- 字符串的大小写转换 --- """
print(stringA.upper())      #全部大写
print(stringA.lower())      #全部小写
print(stringA.capitalize()) #把第一个转换为大写
print(stringA.title())      #把每个单词的第一个转换为大写
print(stringA.swapcase())   #翻转字符串中的大小写



print("\n --- 字符串的文本对齐 --- ")
""" --- 字符串的文本对齐 --- """

print(stringA.ljust(50,"*"))   #字符串.ljust(总长度,填充字符)=>把字符串左对齐,并在右边填充指定的字符
print(stringA.rjust(50,"*"))   #字符串.rjust(总长度,填充字符)=>把字符串右对齐,并在左边填充指定的字符
print(stringA.center(50,"*"))  #字符串.center(总长度,填充字符)=>把字符串居中,并在两边填充指定的字符
print(stringB.zfill(8))        #字符串.zfill(总长度)=>把字符串左对齐,并在右边填充0,直到总长度为50



string_for_explain_del_space = " 字符串去掉空格 "
print("\n",string_for_explain_del_space.center(15,"-"))
""" --- 字符串去掉空格 ---"""
print(stringA.lstrip())        #字符串.lstrip()=>把字符串左边的空格去掉
print(stringA.rstrip())        #字符串.rstrip()=>把字符串右边的空格去掉
print(stringA.strip())         #字符串.strip()=>把字符串两边的空格去掉

print("\n --- 字符串的拆分和拼接 --- ")
""" --- 字符串的拆分和拼接 --- """
print(stringA.split("l",2))       #字符串.split(分隔符,拆分次数)=>把字符串按照指定的分隔符进行拆分,拆分指定次数
print(stringA.rsplit("l",1))      #字符串.rsplit(分隔符,次数)=>把字符串按照指定的分隔符进行拆分,从右边开始拆分,分指定次数
print(stringA.partition("l"))    #字符串.partition(分隔符)=>把字符串按照指定的分隔符进行拆分,返回一个元组
print(stringA.rpartition("l"))   #字符串.rpartition(分隔符)=>把字符串按照指定的分隔符进行拆分,返回一个元组


stringE="Chat\nGPT"
print(stringE)
print(stringE.splitlines())      #字符串.splitlines()=>把字符串按照换行符(\r \n \r\n)进行分

# \r 表示回车符（Carriage Return）
# \n 表示换行符（Newline）。
print("字符“T”的索引:",stringE.index("T"))
print(stringE[-1])

stringF="0"
print(stringF.join("123")) #拼接字符串,在元素之间添加