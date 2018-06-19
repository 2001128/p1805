id_card = {'name':'董帅','birthday':'2001.1.28','sex':'男','address':'山东菏泽'}
print(id_card)
id_card['eth']="汉族"
print(id_card)
id_card['123']="456"
print(id_card)
id_card.setdefault("happy","跑步")
print(id_card)
id_card["height"]=175
print(id_card)
id_card.pop('happy')
print(id_card)
print(id_card["name"])#如果key不在 报错
print(id_card.get("name"))#如果key不在 返回None
print(id_card["sex"])
id_card["name"]="苳帅"#修改
print(id_card)
id_card["height"]=180
print(id_card)
id_card["name"]="董帅"
print(id_card)
print(id_card["height"])
#del id_card["name"]#系统提供的删除方法
#print(id_card)
id_card.popitem()#随机删除,字典时无序的
print(id_card)
#合并
d = {"weight":150,"book":"语文","hobby":"打球"}
id_card.update(d)#如果key存在，则会覆盖掉
print(id_card)
print(id_card["name"])
#for k,v in id_card.items():
 #   print(k,v)
