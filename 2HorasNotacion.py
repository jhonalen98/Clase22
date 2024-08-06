Tiempo24 = input("Introduce la hora en formato 24 horas (HH:MM): ")

hora, minutos = map(int, Tiempo24.split(':'))

if hora >= 12:
    periodo = 'PM'
    if hora > 12:
        hora -= 12
else:
    periodo = 'AM'
    if hora == 0:
        hora = 12

Tiempo12 = f"{hora}:{minutos} {periodo}"
print(Tiempo12)
