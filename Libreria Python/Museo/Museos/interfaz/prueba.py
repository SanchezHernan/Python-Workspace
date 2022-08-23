'''
Aplicando formatos a fechas y horas (Máscaras)
Las siguientes claves se combinan para aplicar formatos:

%a 	Nombre local abreviado de día de semana
%A 	Nombre local completo de día de semana
%b 	Nombre local abreviado de mes
%B 	Nombre local completo de mes
%c 	Representación local de fecha y hora
%d 	Día de mes [01,31]
%H 	Hora (horario 24 horas) [00,23]
%I 	Hora (horario 12 horas) [01,12]
%j 	Número de día del año [001,366]
%m 	Mes [01,12]
%M 	Minuto [00,59]
%p 	Etiqueta AM o PM
%S 	Segundo
%U 	Nº semana del año. Se considera al Domingo como primer día de semana [00,53]
%w 	Establece el primer día de semana [0(Domingo),1(Lunes)... 6].
%W 	Nº semana del año (Se considera al Lunes como primer día de semana) [00,53]
%x 	Fecha local
%X 	Hora local
%y 	Año en formato corto [00,99]
%Y 	Año en formato largo
%Z 	Nombre de Zona Horaria
'''

""" TIME """
import time
"""
print (time.strftime("%H:%M:%S"))
print (time.strftime("%I:%M:%S"))
print (time.strftime("%d/%m/%y"))
print (time.strftime("%c"))
print (time.strftime("%X"))
print (time.strftime("dia %j semana %U"))

b = time.strftime("4/8/2017")
print(b)
"""

""" DATETIME """

from datetime import datetime, date, timedelta


a = date.today()
print (type(a))
x = datetime.now()
print (type(x))

print ("Fecha y hora = %s" %x)
print ("Fecha y hora en formato ISO = %s" % x.isoformat() )
print (u"Anio = %s" %x.year)
print ("Mes = %s" %x.month)
print ("Dia =  %s" %x.day)
print ("Formato dd/mm/yyyy =  %s/%s/%s" % (x.day, x.month, x.year) )
print ("Hora = %s" %x.hour)
print ("Minutos = %s" %x.minute)
print ("Segundos =  %s" %x.second)
print ("Formato hh:mm:ss = %s:%s:%s" % (x.hour, x.month, x.second) )
print ()
print ("Fecha y hora = %s" %a)
print ("Fecha y hora en formato ISO = %s" % a.isoformat() )
print (u"Anio = %s" %a.year)
print ("Mes = %s" %a.month)
print ("Dia =  %s" %a.day)
print ("Formato dd/mm/yyyy =  %s/%s/%s" % (a.day, a.month, a.year) )


#date a partir de string
time = time.strftime("%d/%m/%y")
x = datetime.strptime(time,"%d/%m/%y")

#date a partir de enteros
y= datetime(2017,8,4) # se puede definir hora datetime(2015,12,31,13,12,45)

#sumar o restar dias a un date
b = timedelta(5)
print ("%s" %(x - b), "%s" %(x + b))

#comparacion con operadores >, <, >=, <=, !=, ==
print (x, y)
print (x>y, x<y, x>=y, x<=y, x!=y, x==y)



""" CALENDAR """
import calendar

#print (calendar.calendar(2017))
#print (calendar.prmonth(2017,9))


hora_actual = datetime.now()
print ("Hora Actual %s:%s:%s" % (hora_actual.hour, hora_actual.minute, hora_actual.second))
hora_actual += timedelta(seconds=120)
print ("Hora Actual + 3hs  %s:%s:%s" % (hora_actual.hour, hora_actual.minute, hora_actual.second))



