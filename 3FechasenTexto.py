meses = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}

fecha_str = input("Introduce la fecha (Ejemplo:15, Febrero 1989): ")

partes = fecha_str.split(',')

dia_str = partes[0].strip()
mes_anio_str = partes[1].strip()
mes_str, anio_str = mes_anio_str.split(' ')

mes = meses[mes_str]
dia = int(dia_str)
anio = int(anio_str)

print(dia, mes, anio)