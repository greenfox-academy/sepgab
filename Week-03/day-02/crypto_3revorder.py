# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    my_file = open(file_name, "r")
    chars = []
    s=''
    message = ""
    for line in my_file:
       chars.append(line)
    message = s.join(chars[::-1])
    print(message)

decrypt("reversed-order.txt")
