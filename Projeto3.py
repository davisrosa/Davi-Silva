def media2(a,s):
    d = (a+s)/2
    print(d)
    return d

def media():
    v1 = int(input(" Digite um valor: "))
    v2 = int(input(" Digite outro valor: "))

    md = (v1+v2)/2

    print(" A média dos valores inseridos é: {}".format(md))
    return md

#media()
#media()
#media()

a = media()
b = media()
c = media()
print("{0}, {1}, {2}.".format(a, b, c))

f = int(input(" Entre com um valor: "))
g = int(input(" Entre com outro valor: "))
h = media2(f,g)