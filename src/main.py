import socket
client_sock = socket.socket()
client_sock.connect(('localhost', 9090))

print("Enter deal ID:")
inputID = int(input())

print("Enter date:")
inputDate = input()

client_sock.send(" ".join([str(inputID), str(inputDate)]).encode("utf8"))


data = client_sock.recv(2048).decode("utf8")
client_sock.close()
business_data = data.split(" ")
print("Sum of credit: {}".format(business_data[0]))
print("Total rest summ of credit: {}".format(business_data[1]))
print("Rest summ of credit after {}: {}".format(inputDate, business_data[2]))