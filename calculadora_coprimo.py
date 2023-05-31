class CalculadoraCoprimo:
    def mdc (x,y):
        if(x>y):
            return mdc(y,x)
        if(x==0):
            return y;
        return mdc(x,y%x)
    
    def QuantosCoprimos (numero_analisado):
        quantos = 0;
        i =1 
        while(i < numero_analisado):
            if(mdc(i,numero_analisado)==1):
                quantos+=1;
            i+=1
        return quantos;
