import cgi
from urllib.parse import urlencode
from CreditPaymentsModule import CreditPayments
import CentroBankModule
from xmlrpc import client

form = cgi.FieldStorage()
client_serv = client.ServerProxy('http://localhost:9999')
risk_serv = client.ServerProxy('http://localhost:9000')


deal_id = int(form.getvalue('dealID'))
deal_date = form.getvalue('dealDate')

pObject = CreditPayments()
summ = pObject.getSummOfCredit(deal_id)
total_rest = pObject.getRestOfCredit(deal_id)
rest_by_date = pObject.getRestOfCredit(id= deal_id, date=deal_date)

client_INN = client_serv.get_INN(deal_id)
client_FIO = client_serv.get_FIO(client_INN)
client_history = risk_serv.get_RiskHistory(client_INN)

found_course = CentroBankModule.find_dollar_course()
found_course = found_course.replace(",", ".")
current_course = float(found_course)

summ/=current_course
total_rest/=current_course
rest_by_date/=current_course

params = urlencode({
        'summ': summ,
        'totalRest': total_rest,
        'restByDate': rest_by_date,
        'currentCourse': current_course,
        'inn' : client_INN,
        'fio': client_FIO,
        'riskHist': client_history
    })



'''file = open('style_sources/newresult.html', 'r', encoding = 'utf-8')
html = file.read()
file.close()'''
html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Результаты расчета</title>
        <link rel="stylesheet" href="/style_sources/resultstylesheet.css">
    </head>
    <body>
        <div class="form-container">
            <h1>Результаты расчета</h1>
            <div class="result-container">
                <div class="result-item">
                    <span class="result-label">Общая сумма (USD):</span>
                    <span class="result-value">{summ}</span>
                </div>
                <div class="result-item">
                    <span class="result-label">Общий остаток (USD):</span>
                    <span class="result-value">{total_rest}</span>
                </div>
                <div class="result-item">
                    <span class="result-label">Остаток на дату (USD):</span>
                    <span class="result-value">{rest_by_date}</span>
                </div>
                <div class="result-item">
                    <span class="result-label">Курс доллара США (USD):</span>
                    <span class="result-value">{current_course}</span>
                </div>
                <div class="result-item">
                    <span class="result-label">ФИО клиента:</span>
                    <span class="result-value">{client_FIO}</span>
                </div>
                <div class="result-item">
                    <span class="result-label">ИНН:</span>
                    <span class="result-value">{client_INN}</span>
                </div>
                <div class="result-item">
                    <span class="result-label">Кредитная история:</span>
                    <span class="result-value">{client_history}</span>
                </div>
            </div>
             <button class="back-button" onclick="window.history.back()">Назад</button>
        </div>
    </body>
    </html>
    """
print(html)