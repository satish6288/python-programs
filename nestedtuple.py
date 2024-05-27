test_tuple = ((4,'gfg',10),(3,'is',8),(6,'best',10))
keys=['key','value','id']
res = []
for sub in test_tuple:
    sub_dict={}
    for i in range(len(keys)):
        sub_dict[keys[i]] = sub[i]
    res.append(sub_dict)
print("the converted dictionary"+str(res))