# 设定两个歌曲信息，songA和songB.
# 这里面的键值对有7对，分别为：歌名、歌手、专辑名、流派、语言、封面、年份.(自己自定义信息)
# 让用户依次输入这些信，把这两个字典添加完毕，然后合并这两个字典；
# 然后删掉字典中的封面信息（键值对），最后打印出来。

songA = {
    "歌名": "",
    "歌手": "",
    "专辑名": "",
    "流派": "",
    "语言": "",
    "封面": "",
    "年份": "",
}
songB = {
    "歌名B": "",
    "歌手B": "",
    "专辑名B": "",
    "流派B": "",
    "语言B": "",
    "封面B": "",
    "年份B": "",
}
print("歌曲A")
songA["歌名"] = input("请输入歌名：")
songA["歌手"] = input("请输入歌手：")
songA["专辑名"] = input("请输入专辑名：")
songA["流派"] = input("请输入流派：")
songA["语言"] = input("请输入语言：")
songA["封面"] = input("请输入封面：")
songA["年份"] = input("请输入年份：")
print(songA)

print("歌曲B")
songB["歌名B"] = input("请输入歌名：")
songB["歌手B"] = input("请输入歌手：")
songB["专辑名B"] = input("请输入专辑名：")
songB["流派B"] = input("请输入流派：")
songB["语言B"] = input("请输入语言：")
songB["封面B"] = input("请输入封面：")
songB["年份B"] = input("请输入年份：")
print(songB)

songA.update(songB)
print(songA)

del songA["封面"]
del songA["封面B"]
print(songA)