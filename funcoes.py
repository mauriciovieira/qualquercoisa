# encoding: utf-8

def funcao1():
    print "esta funcao não faz nada"

def funcao2(x):
    if type(x) == str:
        print "x é uma string", x
    elif type(x) == int:
        print "x é um número inteiro",x
    elif type(x) == float:
        print "x é um número float",x
    else:
        print "ah, tou com preguiça, me mostre o tipo de x aí, vá, na moral, vá", type(x)

def funcao3(par):
    variavel = "bli"
    return par == variavel

def faixa_etaria(idade):
    if 18 <= idade < 60:
        return "adulto"
    elif idade <= 10:
        return "criança"
    elif idade >= 60:
        return "idoso"
    elif 10<idade<18:
        return "adolescente"

#funcao1()
#funcao2("mauricio")
#funcao1()
#funcao2(3)
#funcao2(5.0)
#funcao2([])
#resp1 = funcao3("bli")
#print "O resultado da primeira comparação é", resp1
#resp2 = funcao3("bla")

mauricio = 33
igor = 5
braulio = 80
andre = 16

print "Mauricio é ",faixa_etaria(mauricio)
print "Igor é "    ,faixa_etaria(igor)
print "Bráulio é"  ,faixa_etaria(braulio)
print "André é"    ,faixa_etaria(andre)
