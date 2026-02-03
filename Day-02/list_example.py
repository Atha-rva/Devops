# First Type to Create a List 


# a = [10,'Atharva',20.5,True,[1,2,3]]

# print(type(a))
# print(a)


# append Method
# a.append("New Element")
# print(a)


# Second Type to Create a List

clouds = list()

# print(type(clouds))
# <class 'list'>

clouds.append('AWS')
clouds.append('Azure')
clouds.append('GCP')
clouds.append('IBM Cloud')
clouds.append('Oracle Cloud')
clouds.append('Alibaba Cloud')
clouds.append('Microsoft Azure')
clouds.append('Digital Ocean')
# print(clouds)


# print(dir(clouds))

# print(clouds.count.__doc__)

# <class 'list'>
# Return number of occurrences of value


# print("The World of Famous Cloud Providers are:",clouds[0])

# text = "Atharva"

# print(len(text))


# a = [10,'Atharva',20.5,True,[1,2,3]]
# print(len(a))

# i=0
# for i in range(6):
#     print(clouds[i])

# i=0 
# for i in clouds:
#     print(i)


for cloud in clouds:
    if cloud == 'AWS':
        print(cloud, "is the Market Leader in Cloud Computing.")
    elif cloud == 'Azure' or cloud == 'Microsoft Azure':
        print(cloud, "is the Second Largest Cloud Provider.")
    elif cloud == 'GCP':
        print(cloud, "is Google's Cloud Platform.")
    else:
        print(cloud, "is also a Popular Cloud Provider.")
    