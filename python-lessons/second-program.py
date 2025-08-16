# creates a list (array)

# Index is the position on the list
#           0        1        2
my_list = ["red", "green", "blue"]

# add a new item to the list
my_list.append("yellow")

# insert a new item before the index
my_list.insert(3, "orange")

# remove an item from the list
my_list.remove("green")

print(my_list[3])

# slicing a list
print(my_list)
print(my_list[1:3])
print(my_list)

# For loop
for item in my_list:
    print(item)
    
for i in range(5):
    print("Count: ",i)
    
    
    
# dic/obj
user_profile = {
    "name": "Abraham",
    "age": 30,
    "location": "USA",
    "is_verified": True
}

# print(user_profile)
    
    
# Simple chat messages

# store the list of messages
messages = []

# take the user input
user_input = input("Enter a message: ")

user_message = {
    "role": "user",
    "content": user_input
}

# add the user input to the messages
messages.append(user_message)

#TODO: have the model respond to the user
messages.append({"role": "assistant", "content": "here is a poem..."})

print(messages)

# message_1 = messages[0]

# print(message_1["role"])
# print(message_1["content"])

# show the messages
for message in messages:
    print(f"{message['role']}: {message['content']}")





