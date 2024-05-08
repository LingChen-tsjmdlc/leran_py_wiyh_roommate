# ---字典---

# 1，定义一个字典

# 字典名 = {
#     "key 1"= "value 1",
#     "键2"= "值2",
#     "键3"= "值3",
# }
liHua = {
    "name":"李华",
    "age":18,
    "sex":"男",
    "hobby":"唱歌",
    "height":175,
    "weight":60,
    "address":"北京",
    "phone":"12345678901",
}

# 获取键值对的数量
print(len(liHua))   # len(字典名)

# 获取字典里面的所有键
print(liHua.keys())  #字典名.keys()

# 获取字典里面的所有值
print(liHua.values())  #字典名.values()

# 获取字典里面的所有键值对
print(liHua.items())  #字典名.items()

# 获取字典里面的某个键对应的值
print(liHua["name"])  #字典名["键名"]
print(liHua.get("111")) 

# 删除键值对
del liHua["name"]
# liHua.pop("name")

# 随机删除
liHua.popitem()  # 字典名.popitem()
print(liHua)

# 清空字典
# liHua.clear()  # 字典名.clear()
print(liHua)

# 添加
liHua.update({"name":"李华"})  # 字典名.update({"键" : "值"})
print(liHua)

# 遍历
for i in liHua:
    print("遍历:"+i)

# 修改
liHua["name"] = "小米"  #字典名["键"] = "新值"
print(liHua)

liHua["web"] = "www.bilibili.com"  #字典名["键"] = "新值"
print(liHua)

# 合并

xiaoMing = {
    "name2":"小明",
    "age2":20,
    "sex2":"男",
    "hobby2":"唱歌",
    "height2":180,
    "weight2":70,
    "address2":"上海",
    "phone2":"155568846",
}
liHua.update(xiaoMing)  # 字典名1.update(字典名2)
print(liHua)