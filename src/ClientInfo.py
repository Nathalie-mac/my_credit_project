from xmlrpc.server import SimpleXMLRPCServer
client_server = SimpleXMLRPCServer(('localhost', 9999))

def get_INN(dealID):
    return INN_voc.get(dealID)

def get_FIO(inn):
    return FIO_voc.get(inn)

INN_voc = {
    1 : '10101010',
    2: '20202020',
    3: '20202020',
    4: '30303030'}

FIO_voc = {
    '10101010': 'Иванов Иван Иванович',
    '20202020': 'Петров Петр Петрович',
    '30303030': 'Сидоров Сидор Сидорович'}


client_server.register_function(get_INN, 'get_INN')
client_server.register_function(get_FIO, 'get_FIO')


client_server.serve_forever()
#print(get_FIO(get_INN(1)))