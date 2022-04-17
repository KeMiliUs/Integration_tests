import sqlite3


class CalculatorDB:
    __conn = None

    def __init__(self, database, clear=False):
        self.__conn = sqlite3.connect(database)
        self.__check_bd()
        if clear:
            self.__clear_DB()

    def __check_bd(self):
        try:
            cursor = self.__conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS Macc_result("
                           "num_payment int, rate int, term int, balance int, result text)")
            self.__conn.commit()
        except Exception:
            raise TypeError

    def save_result(self, rate, balance, term, num_payments, result):
        if not isinstance(result, str) or not isinstance(rate, int) or not isinstance(balance, int) or not isinstance(
                term, int) or not isinstance(num_payments, int):
            raise ValueError
        try:
            cursor = self.__conn.cursor()
            cursor.execute('INSERT INTO Macc_result(num_payment, rate, term, balance , result) VALUES(?, ?,?,?,?)',
                           [num_payments, rate, term, balance, result])
            self.__conn.commit()
            return True
        except Exception:
            raise TypeError

    def get_one_example(self, rate, balance, term, num_payments):
        try:
            cursor = self.__conn.cursor()
            Select = "SELECT result FROM Macc_result WHERE " + 'rate = ' + str(rate) + " AND term = " + str(
                term) + " AND balance = " + str(balance) + " AND num_payment= " + str(num_payments)
            # print(Select)
            cursor.execute(Select)
            return cursor.fetchall()
        except Exception:
            raise TypeError

    def __clear_DB(self):
        try:
            cursor = self.__conn.cursor()
            cursor.execute('DELETE FROM Macc_result')
            self.__conn.commit()
        except Exception:
            raise TypeError
