from PyTasky import TaskSystem

client = TaskSystem('API_TOKEN') 

tops = client.getUsers()

ids = [x.id for x in tops]

names = client.getNames(ids)

for x in names:
    print(x)