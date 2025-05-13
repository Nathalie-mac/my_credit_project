from xmlrpc.server import SimpleXMLRPCServer
risk_server = SimpleXMLRPCServer(('localhost', 9000))


def get_RiskHistory(inn):
    return Risk_History_voc.get(inn)

Risk_History_voc = {
    '10101010' : "Хорошая",
    '20202020' : "Плохая",
    '30303030' : "Хорошая",
}

risk_server.register_function(get_RiskHistory, 'get_RiskHistory')
risk_server.serve_forever()
#print(get_RiskHistory('10101010'))