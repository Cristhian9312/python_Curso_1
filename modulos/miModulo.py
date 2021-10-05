import datetime

print(datetime.date.today())

fechaCompleta = datetime.datetime.now()

print(fechaCompleta.year)
print(fechaCompleta.month)

fechaPersonalizada = fechaCompleta.strftime("%d/%m/%y")
print(fechaPersonalizada)