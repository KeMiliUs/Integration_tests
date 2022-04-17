from maccelero_calc import Macceleroc_Calculator
from Macceleroc_database import CalculatorDB
class App():
    db=CalculatorDB(database="test.db", clear=True)
    calc = Macceleroc_Calculator()

if __name__ == '__main__':
    app=App()
    result = app.calc.mac_calculate(100000,6,360,12)
    print(result)
    app.db.save_result(6,100000,360,12, result)
    print(str(app.db.get_one_example(6,100000,360,123)))
