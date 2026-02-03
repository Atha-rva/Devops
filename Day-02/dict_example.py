
# Dict Example 
info = {
    "name":"Atharva Deshmukh",
    "age":21,
    "city":"Pune",
    "is_student":True,
    "courses":["DevOps","Cloud Computing","Python"],
    "married":False,
    "data":{
        "id":1,
        "name":"Mohit Mishra",
    },
    "data1":("Welcome","to","Python","World"),
}

print(info)
print(type(info))

print(info["name"])
print(info["age"])
print(info["city"])
print(info["is_student"])
print(info["courses"])
print(info["married"])
print(info["data"])
print(info["data1"])


print("Welcome to the Zitics",info.get("nam","Not Found"))
print("Welcome to the Zitics",info.get("name"))

# Welcome to the Zitics None
# Welcome to the Zitics Atharva Deshmukh