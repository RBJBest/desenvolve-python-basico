ano = int(input ("INSIRA UM ANO: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print (f"{ano} É UM ANO BISSEXTO")
else:
    print (f"{ano} NÃO É UM ANO BISSEXTO")