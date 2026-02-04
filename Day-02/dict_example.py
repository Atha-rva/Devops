
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

# print(info)
# print(type(info))

# print(info["name"])
# print(info["age"])
# print(info["city"])
# print(info["is_student"])
# print(info["courses"])
# print(info["married"])
# print(info["data"])
# print(info["data1"])


# print("Welcome to the Zitics",info.get("nam","Not Found"))
# print("Welcome to the Zitics",info.get("name"))

# Welcome to the Zitics None
# Welcome to the Zitics Atharva Deshmukh

# info.update({
#     "data2":"Welcome to the Zitics"
# })

# print(info)


# We are Printing Just Keys 

# for x in info:
#     print(x)


# Now I Want to Print a keys for it 

# for x in info.keys():
#     print(x)


# for x in info.values():
#     print(x)


# To Print key and values both at same time 

# for x in info.keys() , info.values():
#     print(x)


# for x in info.items():
#     print(x)


# for key,value in info.items():
#     print(key,value)

