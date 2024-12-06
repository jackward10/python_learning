# "Python + is + an + awesome + language". Split the given string to get a list and join to get another string "Python is an awesome language"

message = "Python + is + an + awesome + language"
message_list = message.split(" + ")
print(message_list)

result = " ".join(message_list)
print(result)