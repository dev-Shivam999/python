ok_type={
    "ok":"ooo",
    "ok1":"ooo",
    "ok2":"ooo",
    "multi":{
"ok":"inoo"
    }
}

# print(ok_type.get("ok"))
# for ok in ok_type:
    # print(ok,ok_type.get(ok))
    
# for key,value in ok_type.items():
#     print(key,value)    
    


# if "ok" in ok_type:
#     print("ok is in ok_type")
# else:
#     print("ok is not in ok_type")

# print(len(ok_type))

ok_type["ok3"]="oko"

# print(ok_type)
# ok_type.pop("ok2")

# ok_type.popitem()

# del ok_type["ok2"]
print(ok_type["multi"]["ok"])

