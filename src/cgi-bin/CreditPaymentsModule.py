import sqlite3
import time
from datetime import date

#from db import cursor

class CreditPayments:

    def __init__(self):
        connection = sqlite3.connect('db_sources/mydatabase.db')
        self.cursor = connection.cursor()
        
    #method convert date from MM.yyyy in unix format
    def get_timestamp(self, x):
        # Calc date in unix format
        date_arr = x.split(".")
        d = date(int(date_arr[1]), int(date_arr[0]), 1)
        unixtime = time.mktime(d.timetuple())
        return unixtime
    
    #method getRestOfCredit
    def getRestOfCredit(self, id, date = None):
        # get summ of credit
        # query payments from DB where deal_id=id AND pdate<=date
        # calculate rest of credit and return it
        summ = self.getSummOfCredit(id)
        if not (date is None):
            sql_query = "SELECT sum(summ) FROM payment WHERE deal_id=? and pdate <= ?"
            self.cursor.execute(sql_query, [(id), self.get_timestamp(date)])
        else:
            sql_query = "SELECT sum(summ) FROM payment WHERE deal_id=?"
            self.cursor.execute(sql_query, [(id)])
        return summ - self.cursor.fetchone()[0]
        pass


    #method getSummOfCredit
    def getSummOfCredit(self, id):
        # query summ of credit from DB where id=id
        # return it
        sql_query = 'Select summ from credit where id =?'
        self.cursor.execute(sql_query, [id])
        summ_of_credit = self.cursor.fetchone()[0]
        return summ_of_credit
