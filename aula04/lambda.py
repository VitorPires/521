x = lambda y: y*2
print(x(2))
print(x)

lista = [lambda x: x**2,
 	 lambda x: x * 3,
         lambda x: x * 4
        ]

for a in lista:
  print(a(10))


