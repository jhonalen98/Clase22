N1=int(input("Ingrese la primera nota: "))
N2=int(input("Ingrese la segunda nota: "))
N3=int(input("Ingrese la tercera nota: "))
N4=int(input("Ingrese la cuarta nota: "))

Media=(N1+N2+N3+N4)/4
print(Media)

if Media >89 and Media < 101:
    print("Su puntuación es A")
elif Media > 79:
    print("Su puntución es B")
elif Media > 69:
    print("Su puntución es C")
elif Media > 59:
    print("Su puntución es D")
elif Media > 0:
    print("Su puntuación es E")