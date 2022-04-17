def My_Floor(number):
    if (number - int(number) >= 0.5):
        return int(number) + 1
    else:
        return int(number)
class Macceleroc_Calculator:
    @staticmethod
    def mac_calculate(balance:int, rate: float ,term: int, num_payments: int) -> str:
        Rate= rate/1200
        if(num_payments>term):
            raise ValueError
        if(rate < 0):
            raise  ValueError
        if (balance < 0):
            raise ValueError
        d=1-(1+Rate)**(-1*term)
        n=balance *Rate
        if( d==0):
            c =balance/term
        else:
            c=n/d
        Int = 0
        princ = 0
        Balance = balance +0
        for i in range(num_payments):
            Int=Balance*Rate
            princ=c-Int
            Balance=Balance - princ
        if(Balance<0):
            balance=0
        c=My_Floor(c)
        princ = My_Floor(princ)
        Int = c-princ
        Balance = My_Floor(Balance)
        result = "num_payment " + str(num_payments)+" c " + str(c) + " princ " + str(princ) +" Int "+str(Int)+ " balance "+ str(Balance)
        return result
