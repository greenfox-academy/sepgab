# Things are a little bit messed up
# Your job is to decode the notSoCrypticMessage by using the hashmap as a look up table
# Assemble the fragments into the out variable

out = "";
notSoCrypticMessage = [1, 12, 1, 2, 11, 1, 7, 11, 1, 49, 1, 3, 11, 1, 50, 11]

hashmap = [
    {7: "run around and desert you"},
    {50: "tell a lie and hurt you"},
    {49: "make you cry,"},
    {2: "let you down"},
    {12: "give you up,"},
    {1: "Never gonna"},
    {11: "\n"},
    {3: "say goodbye"}
]

list_message = []

for i in range(0, len(notSoCrypticMessage)):
    for j in range(0, len(hashmap)):
        for key, value in hashmap[j].items():
            if notSoCrypticMessage[i] == key:
                list_message.append(value)

out = ' '.join(list_message)

print(out)
