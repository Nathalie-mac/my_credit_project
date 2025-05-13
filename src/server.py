from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print("HTTP server started on ip: %s, port: %s" % server_address)

httpd.serve_forever()

'''
local_sock = socket.socket()
local_sock.bind(('', 9090))
local_sock.listen(1)
connect, addr = local_sock.accept()

while True:
    data = connect.recv(2048)
    if not data:
        break
    a = data.decode("utf8")
    if a:
        business_data = a.split(" ")
        pObject = CreditPayments()
        summ = pObject.getSummOfCredit(int(business_data[0]))
        totalRest = pObject.getRestOfCredit(int(business_data[0]))
        restByDate = pObject.getRestOfCredit(id=int(business_data[0]), date=business_data[1])
        connect.send(" ".join([str(summ), str(totalRest), str(restByDate)]).encode("utf8"))
    else:
        connect.send("Invalid data".encode("utf8"))
'''