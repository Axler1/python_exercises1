# def tri_recursion(ko):
#  if ko > 0:
#    testingRename = ko  + tri_recursion(ko - 1)
#    print(testingRename)
#  else:
#    testingRename = 0

#    return testingRename

# def mi_funcion(parametro):
#  return parametro + 2

# print(mi_funcion(2))

# while True:
#  if x < 10:
#      print('this is nice')
# else:
#     print('this is a function ok')


# while  x:
#  for  i,y in list(range(6)):
#    print(i+y)

#  def  testing():
#    doc = """This is nice"""
#    def fget(self):
#      return self._ testing

#    def fset(self, value):
#      self._ testing = value

# #      def fdel(self):
# #        del self._ testing
# #        return locals()
# #      testing = property(** testing())

# #w


# ## 5 + (4 + (3 + (2 + (1 + 0))))
# ##
# ## -------------------------------
# ## Definir una función la cual nos permita convertir un string a un formato título. es entiende por formato título un string con su primera letra en mayúscula.
# ## - la función debe tener por nombre to_title.
# ## - la función debe poser el parámetro message.
# ## - el parámetro debe ser obligatorio.
# ## - la función debe retornar el parámetro en su formato título.

# ## def to_tile(message):
# ##     return message.title()
# ## print(to_tile(input('ingrese el texto: ')))

# ## def to_title(message):
# ##     return message[0].upper() + message[1:]

# ## print(to_title('pedro la rosa'))
# ## -------------------------------
# ## desarrolla un programa en python para convertir pies a centímetros.
# ## el usuario podrá ingresar, vía teclado, los pies de los cuales desea conocer su equivalente en cm.
# ## el programa debe imprimir en consola el equivalente a centímetros.

# #for i in list(range(6)):
# #  print(i+1)

# ## def conversion(valor):
# ##     if valor >= 0:
# ##         x = valor * 30.48
# ##         return f"{x} cm"

# ## print(conversion(float(input('ingrese la cantidad de pies: '))))


# ## -------------------------------
# ## solicitar al usuario que ingrese su dirección email. imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. una dirección se considerará válida si contiene el símbolo "@".

# ## def validacion(mail):
# ##     if '@' in mail:
# ##         return 'direccion válida'
# ##     else:
# ##         return 'direccion no válida'

# ## print(validacion(input('ingrese su email: ')))
# ## -------------------------------
# ## solicitar números al usuario hasta que ingrese el cero. por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).

# #def suma(numero):
# #    while True:
# #        if numero >= 0:
# #            continue
# #        else:
# #            print(1.2)
# #            break

# #suma(5)
# #print(suma(int(input('ingrese los numeros: '))))

# #def sumadigitos(numero):
# #    suma=0
# #    while numero!=0:
# #        digito=numero%10
# #        print('digito:',digito)

# #        suma=suma+digito
# #        print('suma:',suma)

# #        # numero=numero//10
# #        # print('numero:',True)

# #    # return sum


# ## def sumafinaldigitos(z):
# ##     w = z % 10
# ##     print('w es:',w)

# ##     z = z // 10
# ##     print('z es:',z)

# ##     return w + z


# ## todoslosnumeros = list()
# ## num=int(input("número a procesar: "))
# ## todoslosnumeros.append(num)

# ## while num!=0:
# ##     print("sumar:",sumadigitos(num))
# ##     num=int(input("número a proces: "))
# ##     todoslosnumeros.append(num)

# ## print(todoslosnumeros)
# ## x = sum(todoslosnumeros)
# ## print(x)

# ## print(sumafinaldigitos(x))


# ## -------------------------------
# ## requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

# ## def primo(num):
# ##     if num < 2:
# ##         return false

# ## for i in range(2,num):
# ##    if num % i == 0:
# ##        return false
# ## return true


# ## numero=int(input("número: "))
# ## if primo(numero):
# ##     print("es primo")
# ## else:
# ##     print("no es primo")

# ## -------------------------------
# ## solicitar al usuario un número entero y luego un dígito. informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.

# ## def frecuenci(num, dig):
# ##     if dig in num:
# ##         return 'la frecuencia del dígito es:',num.count(dig)
# ##     return 'no se encontro ocurrencias',num, dig

# ## print(frecuenci(input('ingrese un número: '), input('ingrese un dígito: ')))

# ## def frecuencia(numero,digito):
# ##    cantidad=0
# ##    while numero!=0:
# ##        ultdigito=numero%10
# ##        print('uldigito es:',ultdigito)
# ##        if ultdigito==digito:
# ##            cantidad+=1
# ##        numero=numero//10
# ##    return cantidad


# ## num=int(input("número: "))
# ## un_digito=int(input("dígito: "))
# ## print("frecuencia del dígito en el número:",frecuencia(num,un_digito))

# ## -------------------------------
# ## escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. utilizar una o más funciones, según sea necesario.

# ## def factorial(num):
# ##     if num > 0:
# ##         x = num * factorial(num - 1)
# ##     else:
# ##         x = 1

# ##     return x

# ## # 5 * ( 4 * ( 3 * ( 2 * ( 1 * 1))))
# ## # print(factorial(5))
# ## def totalnumeros(arg):
# ##     return 'numeros leidos en total:',len(arg)

# ## numerosingresados = list()
# ## numero = -1
# ## while numero != 0:
# ##     # cuenta += 1
# ##     numero = int(input('ingrese el numero: '))
# ##     print(factorial(numero))
# ##     numerosingresados.append(numero)

# ## print(totalnumeros(numerosingresados))

# ## def factorial(numeros):
# ##    f = 1
# ##    if numeros != 0:
# ##        for i in range(1,numeros + 1):
# ##            f = f * i
# ##    return f


# ## if
# ## cantidad = 0
# ## num = int(input("número (-1 para cortar): "))
# ## while num != -1:
# ##     print("factorial:", factorial(num))
# ##     cantidad += 1
# ##     num = int(input("número (-1 para cortar): "))
# ## print("se leyeron",cantidad,"números")


# ## -------------------------------
# ## el siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. ¿qué hay que corregir?

# ## def maximo(a,b):
# ##   if a>b:
# ##     return a
# ##   else:
# ##     return b


# ## def minimo(a,b):
# ##   if a<b:
# ##     return a
# ##   else:
# ##     return b


# ## programa principal
# ##x=int(input("un número: "))
# ##y=int(input("otro número: "))
# ##print(maximo(x-3, minimo(x+2, y-5)))

# ## -------------------------------
# ## escribir una función que, dado un string, retorne la longitud de la última palabra. se considera que las palabras están separadas por uno o más espacios. también podría haber espacios al principio o al final del string pasado por parámetro.

# ## def laststring(arg1):
# ##     if len(arg1) == 0:
# ##         return 0
# ##     else:
# ##         listadestrings = arg1.split()
# ##         ultimapalabra = len(listadestrings) - 1
# ##         x = len(listadestrings[ultimapalabra])
# ##         return f'la longitud de la última palabra es: {x}'

# ## texto = input('ingrese el texto: ')
# ## print(laststring(texto))


# ## def lenultimapalabra(frase):
# ##     if len(frase) == 0:
# ##         return 0
# ##     cantidad = 0
# ##     for i in range(len(frase)):
# ##         if frase[i] != ' ':
# ##             cantidad += 1
# ##         else:
# ##             if i < len(frase)-1 and frase[i+1] != ' ':
# ##                 cantidad = 0
# ##     return cantidad

# ## texto = input('ingrese el texto: ')
# ## print(lenultimapalabra(texto))




# # # -------------------------------
# # # Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. para eso ingresará nombre completo y número de dni de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.
# ## Precondición: el formato del nombre de los socios será: nombre apellido. podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. si un socio tuviera más de un apellido, el usuario sólo ingresará uno.
# ## se debe validar que el número de dni tenga 7 u 8 dígitos. en caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un dni correcto.
# ## Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su dni. ejemplo:
# ## nombre: alba maría linares
# ## dni: 25834910
# ## alba7258



# ## def nombresapellido(x):
# ##     while true:
# ##         if len(x) == 0:
# ##             break
# ##         else:
# ##             lista = x.split(' ')
# ##             if len(lista) == 4:
# ##                 del lista[3]
# ##                 return f'{lista[0]}{len(lista[2])}'
# ##             elif len(lista) == 3:
# ##                 return f'{lista[0]}{len(lista[2])}'

# ## def cdni(y):
# ##     while true:
# ##         if len(y) == 0:
# ##             break
# ##         else:
# ##             if len(y) == 7 or len(y) == 8:
# ##                 return y[:3]
# ##             else:
# ##                 y = input('ingrese correctamente el dni: ')

# ## texto = input('ingrese su nombre: ')
# ## nombresapellido(texto)
# ## dni = input('ingrese el dni: ')
# ## cdni(dni)

# ## print(f'{nombresapellido(texto)}{cdni(dni)}')



# #def lenultimapalabra(cadena):
# #   longitud=len(cadena)
# #   if longitud==0:
# #       return 0
# #   cantidad=0
# #   for i in range(longitud):
# #       if cadena[i]!=' ':
# #           cantidad+=1
# #       else:
# #           if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
# #               cantidad=0
# #   return cantidad


# #def dnivalido(dni):
# #   cantidad=0
# #   while dni!=0:
# #       cantidad+=1
# #       dni//=10
# #   return cantidad==7 or cantidad==8


# ## def primerostresdigitos(numero):
# ##    while numero >= 1000:
# ##      numero = numero // 10
# ##    return numero


# ## def obteneridentificador(nombre, dni):
# ##    nombre=nombre.strip()
# ##    id=nombre[:nombre.find(" ")]
# ##    id=id+str(lenultimapalabra(nombre))
# ##    id=id+str(primerostresdigitos(dni))
# ##    return id


# #programa principal
# #nombre=input("nombre del socio: ")
# #while nombre!="":
# #  dni=int(input("dni del socio: "))
# #  while dni != 7 or dni != 8:
# #     print("número inválido.")
# #     dni=int(input("dni del socio: "))
# #  print(obteneridentificador(nombre,dni))
# #  nombre=input("nombre del socio: ")


# ## -------------------------------
# ## Escribir la función titulo(), la cual recibe un string y lo retorna
# ## convirtiendo la primera letra de cada palabra a mayúscula y las demás letras
# ## a minúscula, dejando inalterados los demás caracteres. precondición: el
# ## separador de palabras es el espacio: " ". agregar doctests con suficientes
# ## casos de prueba para validar que la función retorna el valor esperado ante
# ## distintos argumentos.

# ## def titulo(x):
# ##     if len(x) == 0:
# ##         return ''
# ##     else:
# ##         renombrando = list()
# ##         x = x.lower()
# ##         x = x.replace(' ', '#')
# ##         lista = x.split('#')
# ##         for nice in lista:
# ##             if len(nice) == 0:
# ##                 renombrando.append(nice)
# ##                 continue
# ##             elif len(nice) != 0 and nice.isalpha() == True:
# ##                 may = nice[0].upper()
# ##                 z = may+nice[1:]
# ##                 renombrando.append(z)
# ##             elif len(nice) != 0 and nice.isalnum() == True:
# ##                 isnum = nice[0]
# ##                 if isnum.isdigit() == True:
# ##                     w = isnum+nice[1:].capitalize()
# ##                     renombrando.append(w)
# ##                 if isnum.isdigit() == True:
# ##                     t = nice.capitalize()
# ##                     renombrando.append(t)
# ##             elif len(nice) != 0 and nice.isalnum() == False:
# ##                     b = nice[0:2]+nice[2:].capitalize()
# ##                     renombrando.append(b)
# ##         return ' '.join(renombrando)


# ## texto = input('ingrese el texto: ')
# ## print(titulo(texto))


# ## def titulo(cadena):
# ##     '''
# ##     recibe una cadena de caracteres y retorna una copia que tiene la
# ##     primera letra de cada palabra en mayúsculas y el resto de las letras
# ##     en minúsculas.
# ##     >>> titulo('esto es una frase')


# ## #     'esto es una frase'
# ## #     >>> titulo('esto es una frase')
# ## #     'esto es una frase'
# ## #     >>> titulo('palabra')
# ## #     'palabra'
# ## #     >>> titulo('   esto es una frase')
# ## #     '   esto es una frase'
# ## #     >>> titulo('esto es una frase   ')
# ## #     'esto es una frase   '
# ## #     >>> titulo('esto   es   una   frase')
# ## #     'esto   es   una   frase'
# ## #     >>> titulo('')
# ## #     ''
# ## #     >>> titulo(' ')
# ## #     ' '
# ## #     >>> titulo('123')
# ## #     '123'
# ## #     >>> titulo('-1esto 2es 3una 4frase')
# ## #     '-1esto 2es 3una 4frase'
# ## #     >>> titulo('esto1 es2 una3 frase4---')
# ## #     'esto1 es2 una3 frase4---'
# ## #     '''
# ##     nuevas = ""
# ##     iniciopalabra=True              #indica el inicio de una palabra
# ##     for caracter in cadena:
# ##         if not caracter.isalpha():
# ##             nuevas=nuevas+caracter
# ##             iniciopalabra=True
# ##         else:
# ##             if iniciopalabra:
# ##                 nuevas=nuevas+caracter.upper()
# ##                 # print(nueva)
# ##                 iniciopalabra=False  #ya no es el inicio de una palabra
# ##             else:
# ##                 nuevas=nuevas+caracter.lower()
# ##                 # print(nueva)
# ##     return nuevas



# ## texto = input('ingrese el texto: ')
# ## print(titulo(texto))

# ## def como_titulo(texto):
# ##     return texto.title()

# ## print(como_titulo(input('Ingrese el texto: ')))


# ## x = 12
# ## def g(x):
# ##       print(f'x before: {x}')
# ##       x = x + 1
# ##       print(f'x after: {x}')
# ##       def h(y):
# ##           return x + y
# ##       return h(6)
# ## print(g(x))


# ## def iterPower(base, exp):
# ##     '''
# ##     base: int or float.
# ##     exp: int >= 0

# ##     returns: int or float, base^exp
# ##     '''
# ##     x = 1
# ##     count = 1
# ##     while count <= exp:
# ##         x = x * base
# ##         count += 1
# ##     return x

# ## print(iterPower(2, 5))



# ## def recurPower(base, exp):
# ##     '''
# ##     base: int or float.
# ##     exp: int >= 0

# ##     returns: int or float, base^exp
# ##     '''
# ##     if exp == 0:
# ##         base = 1
# ##         exp = 1
# ##         return base * exp
# ##     # if exp == 1:              # Cuando se multiplica por exp == 1 se retorna automáticamente la base, entonces no es necesario establecer una condición
# ##     #     return base * exp
# ##     else:
# ##         # print(exp)
# ##         return base * recurPower(base, exp - 1)
# ##     # 2 * (2 * (2 * (2 * (1))))

# ## print(recurPower(2, 4))

# ## def gcdIter(a, b):
# ##     '''
# ##     a, b: positive integers

# #    # returns: a positive integer, the greatest common divisor of a & b.
# #    # '''
# #    if a > b:
# #        number = b
# #    else:
# #        number = a

# #    for i in range(min(a, b), 0, -1):
# #        print(i)

# #    while True:
# #        if number == 1:
# #            return number
# #        if a % number == 0 and b % number == 0:
# #            return number
# #        number -= 1

# #    # while a % number != 0 or b % number != 0:
# #    #     number -= 1
# #    # return number

# ## print(gcdIter(17, 12))


# ## gcd(a, b)       == gcd(b, a % b)

# ## gcd(1071, 462)  == gcd(462, 1071 % 462 == 147)
# ## gcd(1071, 462)  == gcd(147, 462 % 147 == 21)
# ## gcd(1071, 462)  == gcd(21, 147 % 21 == 0)


# ## def gcdRecur(a, b):
# ##     '''
# ##     a, b: positive integers

# #    # returns: a positive integer, the greatest common divisor of a & b.
# #    # '''
# #    # if b == 0:  # Estableciendo el caso base
# #    #     return a
# #    # else:
# #    #     # print(a, b)
# #    #     return gcdRecur(b, a % b)   # Invierto el orden de los parámetros al llamar a la función
# #    #      462, 147
# #    #      147, 21
# #    #      21, 0

# ## print(gcdRecur(0, 17))


# ## def fib(x):
# ##     """assumes x an int >= 0 returns Fibonacci of x"""
# ##     if x == 0 or x == 1:
# ##         # print('x',x)
# ##         return 1
# ##     else:
# ##         print(x)
# ##         return fib(x-1) + fib(x-2)
# ## f(3) + f(2)
# ## [f(2) + f(1)] + f(2)
# ## [f(2) + f(1)] + [f(1) + f(0)]
# ## [{f(1) + f(0)} + f(1)] + [f(1) + f(0)]
# ## [{1 + 1} + 1] + [1 + 1]
# ## == 5
# ## print(fib(4))


# ## def isPalindrome(s):

# ##     def toChars(s):
# ##         s = s.lower()
# ##         ans = ''
# ##         for c in s:
# ##             if c in 'abcdefghijklmnopqrstuvwxyz':
# ##                 ans = ans + c
# ##         return ans

# ##     def isPal(s):
# ##         if len(s) <= 1:
# ##             return True
# ##         else:
# ##             print(s[1:-1])  # The argument 's' is updated after every function call
# ##             return s[0] == s[-1] and isPal(s[1:-1])

# ##     return isPal(toChars(s))

# ## print(isPalindrome(input('Texto: ')))



# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string

#     returns: True if char is in aStr; False otherwise
#     '''
#     def alpha(aStr):
#         aStr = aStr.lower()
#         aStr = sorted(aStr)
#         alpha = ""
#         for i in aStr:
#             if i != " ":
#                 alpha = alpha + i
#         # mitad = len(alpha) // 2
#         # return alpha, mitad, alpha[:mitad], alpha[mitad:]
#         return alpha

#     def check(char, aStr):
#         if len(aStr) == 0 or len(aStr) == 1 and char != aStr: # Al parecer esta línea evalua lo siguiente: p or (q and r)
#             return False
#         # if len(aStr) == 1 and char != aStr[0]:
#         #     return False

#    # Base case: if aStr is of length 1, just see if the chars are equal
#       if len(aStr) == 1:
#       return aStr == char           # Otra forma de retornar el valor y permitir que retorne 'True' or 'False' independienmete de que se establezca que return solo un determinado valor

#       else:
#            mitad = len(aStr) // 2
#            if char == aStr[mitad-1]:
#                return True
#            if char > aStr[mitad-1]:
#                return check(char, aStr[mitad:])
#            if char < aStr[mitad-1]: # ó mejor 'else' pues ya se establecio en la línea 615 lo contrario
#                return check(char, aStr[:mitad-1])

#     return check(char, alpha(aStr))

# print(isIn('n','esteNtest'))

# def oddTuples(aTup):
#     laTupla = ()
#     for i in range(len(aTup)):
#         if i % 2 == 0:
#             laTupla = laTupla + (aTup[i],)
#     return laTupla


# print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))


# ----- Looking for the most common words and the often words in a song lyrics

# she_loves_you = ['it', 'is','is','is','is','is','is','is','is','is','she','she', 'she', 'loves','loves','loves', 'yeah','yeah', 'yeah','yeah','yeah','yeah','yeah','yeah','yeah', 'you', 'you','you']

# def lyrics_to_frequencies(lyrics):
#     myDict = {}
#     for word in lyrics:
#         if word in myDict:
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
#     return myDict

# beatles = lyrics_to_frequencies(she_loves_you)

# def most_common_words(freqs):
#     # values = freqs.values()
#     best = max(freqs.values())
#     words = []
#     for k in freqs:
#         if freqs[k] == best:
#             words.append(k)
#     return (words, best)

# # most_common_words(beatles)

# def words_often(freqs, minTimes):
#     result = []
#     done = False
#     while not done:
#         temp = most_common_words(freqs)
#         if temp[1] >= minTimes:
#             result.append(temp)
#             for w in temp[0]:
#                 del(freqs[w])
#         else:
#             done = True
#     return result

# print(words_often(beatles, 3))

# ----- First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:

# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.

#     returns: int, how many values are in the dictionary.
#     '''
#     # valores = list(aDict.values())
#     # maximo = len(max(valores))
#     # print(max(aDict.values()))
#     mayor = 0
#     for j in aDict.values():
#         if len(j) > mayor:
#             mayor = len(j)

#     for l in aDict.keys():
#         if len(aDict[l]) == mayor:
#             return l
#         # elif len(aDict[l]) == 0:
#         #     return None
#     # return eval('[' + ', '.join(str(v)[1:-1] for v in aDict.values()) + ']')   # For retrieving the dict all the dict values in a list

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'] }

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# print(animals)
# animals = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}
# animals = {'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}
# animals = {'u': []}
# print(how_many(animals))

# def biggest(aDict):
#     keys_list = []
#     values_list = []
#     for i in aDict:
#         keys_list.append(i)
#         values_list.append(len(aDict[i]))

#     print(values_list.index(max(values_list)))
#     return keys_list[(values_list.index(max(values_list)))]

# def biggest(aDict):
#      key_lngst_val = None
#      klv_len = 0
#      for k in aDict:
#          if len(aDict[k]) >= klv_len:
#              key_lngst_val = k
#              klv_len = len(aDict[k])
#      return key_lngst_val

# def biggest(aDict):
#     return max((len(aDict[k]), k) for k in aDict)[1]

# print(biggest(animals))
# timeit("biggest(animals)", globals=globals())   # Time measurement. Timeit runs 1 Million iterations to increase measurement reliability.

# ----- Fibonacci and Dictionaries

# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fib(n-1) + fib(n-2)

# def fib_efficient(n, d):
#     global numFibCalls
#     numFibCalls += 1
#     if n in d:
#         return d[n]
#     else:
#         ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
#         d[n] = ans
#         return ans

# d = {1:1, 2:2}
# numFibCalls = 0

# print(fib_efficient(5, d),'\nllamadas a la función:',numFibCalls)

# def maxOfThree(a,b,c) :
#     """
#     a, b, and c are numbers

#     returns: the maximum of a, b, and c
#     """
#     if a > b:
#         bigger = a

#     else:
#         bigger = b

#     if c > bigger:
#         bigger = c

#     return bigger

# maxOfThree(-10,0,30)

# def rem(x, a):
#     """
#     x: a non-negative integer argument
#     a: a positive integer argument

#     returns: integer, the remainder when x is divided by a.
#     """
#     if x == a:
#         return 0
#     elif x < a:
#         return x
#     else:
#         return rem(x-a, a)

# rem(7,5)


# def get_ratios(L1, L2):
#     """Assumes: L1 and L2 are list of equal length of numbers
#        Return: a list containing L1[i]/L2[i]"""
#     ratios = []
#     for index in range(len(L1)):
#         try:
#             ratios.append(L1[index]/float(L2[index]))
#         except ZeroDivisionError:
#             ratios.append(float('NaN'))  # NaN means not a number
#         except:
#             raise ValueError('get_ratios called with bad arg')
#     return ratios

# def fancy_divide(list_of_numbers, index):
#    denom = list_of_numbers[index]
#    return [simple_divide(item, denom) for item in list_of_numbers]


# def simple_divide(item, denom):
#     try:
#         return item / denom
#     except ZeroDivisionError:
#         return denom


# print(fancy_divide([0, 2, 4], 0))

# class Coordinate(object):
#    not_int_init_attribute = "I am not in __init__"     # Defining a data attribute within the class definition that is not in '__init__'
#    def __init__(self, x, y):  # '__init__' method to create an instance; 'self' parameter to refer to an instance of the class
#       self.x = x
#       self.y = y
#    def distance(self, other):
#       x_diff_sq = (self.x-other.x)  ** 2  # dot notation to access data
#       y_diff_sq = (self.y-other.y) ** 2  # get value of 'other' in that created frame, define variable bindings for x and y and retrieve to variable bindings
#       return (x_diff_sq + y_diff_sq) ** 0.5

# c = Coordinate(3,4)
# origin = Coordinate(0,0)
# print(c.distance(origin))  # the 'c' instance is automatically used as 'self' argument for 'distance' method
# # or
# # print(Coordinate.distance(c, origin))   # 'c' instance is manually used  as 'self' argument for 'distance' method

# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         print(self.time)

# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()

# Something like duplicate_clock = Clock(boston_clock.time) would do the trick.

# ----- Example: Fractions
# class fraction(object):
#    def __init__(self, numer, denom):
#       self.numer = numer
#       self.denom = denom
#    def __str__(self):
#       return str(self.numer) + ' / ' + str(self.denom)
#    def getNumer(self):
#       return self.numer
#    def getDenom(self):
#       return self.denom
#    def __add__(self, other):
#       numerNew = other.getDenom() * self.getNumer() \
#                  + other.getNumer() * self.getDenom()
#       denomNew = other.getDenom() * self.getDenom()
#       return fraction(numerNew, denomNew)
#    def __sub__(self, other):
#       numerNew = other.getDenom() * self.getNumer() \
#                  - other.getNumer() * self.getDenom()
#       denomNew = other.getDenom() * self.getDenom()
#       return fraction(numerNew, denomNew)
#    def convert(self):
#       return self.getNumer() / self.getDenom()  # Operating and returning a floating point

# oneHalf = fraction(1,2)
# twoThirds = fraction(2,3)
# print(oneHalf)
# print(twoThirds)

# print(oneHalf.getNumer())
# new = oneHalf + twoThirds
# print(new)

# threeQuarters = fraction(3,4)
# print(threeQuarters)

# secondNew = twoThirds - threeQuarters
# print(secondNew)

# print(twoThirds.convert())


# # ----- Example: A set of integers
# class intSet(object):
#    def __init__(self):
#       self.vals = []
#    def insert(self, e):
#       if not e in self.vals:
#          self.vals.append(e)
#    def member(self, e):
#       return e in self.vals
#    def remove(self, e):
#       try:
#          self.vals.remove(e)
#       except:
#          raise ValueError(str(e) + ' not found') # from None, if getting and error when number is not in the set
#    def __str__(self):
#       self.vals.sort()
#       result = ''
#       for e in self.vals:
#          result = result + str(e) + ','
#       return '{' + result[:-1] + '}'

# s = intSet()
# print(s)

# s.insert(3)
# s.insert(4)
# print(s)

# s.remove(8)
# print(s)

# print(s.member(8))

# ----- Finger Exercise

# class Coordinate(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def getX(self):
#         # Getter method for a Coordinate object's x coordinate.
#         # Getter methods are better practice than just accessing an attribute directly
#         return self.x

#     def getY(self):
#         # Getter method for a Coordinate object's y coordinate
#         return self.y


#     def __str__(self):
#         return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

#     def __eq__(self, other):
#        return other.getX() == self.getX() and other.getY() == self.getY()

#     def __repr__(self):
#        return 'Coordinate'  + '(' + str(self.getX()) + ',' + str(self.getY()) + ')'
#        return Coordinate(self.getX(), self.getY())

# str creates a string representation you want when someone goes print(myobj)

# repr creates a string representation that you want to be able to be evaluated to give the same result as running the object with eval(myobj)

# but if you have a repr and no str then the interpreter will use the repr as a substitute for str in print.

# When you go print(object) you are running the function print which calls its __str__ method for a string to print.

# When you go repr(object) you are running the function repr which calls its __repr__ method for a string to print.


# And if there is no dunder str for an object print will print its dunder repr as backup.
#  If neither theres a built in fallback to some kind of object representation.

# repr creates a string representation that you want to be able to be evaluated to give the same result as running the object with eval(myobj)

# c = Coordinate(3,7)
# print(c)
# a = Coordinate(3,7)
# print(c.__eq__(a))

# print(c.__repr__())
# print(repr(c))


# class intSet(object):
#     """An intSet is a set of integers
#     The value is represented by a list of ints, self.vals.
#     Each int in the set occurs in self.vals exactly once."""

#     def __init__(self):
#         """Create an empty set of integers"""
#         self.vals = []

#     def insert(self, e):
#         """Assumes e is an integer and inserts e into self"""
#         if not e in self.vals:
#             self.vals.append(e)

#     def member(self, e):
#         """Assumes e is an integer
#            Returns True if e is in self, and False otherwise"""
#         return e in self.vals

#     def remove(self, e):
#         """Assumes e is an integer and removes e from self
#            Raises ValueError if e is not in self"""
#         try:
#             self.vals.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')

#     def getList(self):
#         return self.vals

#     def __len__(self):
#         try:
#             return self.getList().index(self.getList()[-1]) + 1
#         except IndexError:
#             return 0

#     # def intersect(self, other):
#     #     self.aList = []
#     #     for i in self.getList():
#     #         for j in other.getList():
#     #             if i == j:
#     #                 self.aList.append(i)
#     #     self.aList.sort()
#     #     return '{' + ','.join([str(e) for e in self.aList]) + '}'

#     def intersect(self, other):
#         """Returns an intersection of two intSets"""
#         rslt = intSet()
#         for i in self.vals:
#             if i in other.vals:
#                 rslt.insert(i)
#         return rslt

#     def __str__(self):
#         """Returns a string representation of self"""
#         self.vals.sort()
#         return '{' + ','.join([str(e) for e in self.vals]) + '}'

# # You have to start by creating a decent init for intSet then it becomes pretty easy.

# class intSet(object):
#     def __init__(self, *v):
#         self.vals = (sorted(set(v) if len(v)>1 or isinstance(*v, int) else set(*v))) if v else []
#     def insert(self, e):
#         self.vals.append(self.vals.pop() if e in self.vals else e)
#     def member(self, e):
#         return e in self.vals
#     def remove(self, e):
#         try:
#             self.vals.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')
#     def intersect(self, other):
#         return intSet(i for i in self.vals if i in other.vals)
#     def __eq__(self, other):
#         return self.vals == other.vals
#     def __len__(self):
#         return len(self.vals)
#     def __str__(self):
#         return '{' + ','.join([str(e) for e in sorted(self.vals)]) + '}'
#     def __repr__(self):
#         return '{' + ','.join([str(e) for e in sorted(self.vals)]) + '}'

# # or if you subclass set then you have a simpler:

# class intSet(set):
#     def insert(self, e):
#         self.add(e)
#     def member(self, e):
#         return e in self
#     def remove(self, e):
#         if e in self:
#             self.discard(e)
#         else:
#             raise ValueError(str(e) + ' not found')
#     def intersect(self, other):
#         return intSet(i for i in self if i in other)
#     def __str__(self):
#         return '{' + ','.join([str(e) for e in sorted(self)]) + '}'
#     def __repr__(self):
#         return __str__(self)


# l1 = [0,1,3,4,7]
# l1 = [0,8,3,9,5]

# s = intSet()
# print(s)
# s.insert(3)
# s.insert(4)
# s.insert(5)
# print(s)
# print(s.member(3))

# t = intSet()
# print(t)
# t.insert(3)
# # t.insert(4)
# t.insert(5)
# t.insert(11)
# t.insert(12)
# t.insert(10)
# print(t)

# print(s.getList())
# print(t.getList())

# print(s.intersect(t))
# print(s.__len__())
# print(len(s))
# print(t.__len__())

# a = intSet()
# a.insert(5)
# print(a)
# print(len(a))

# Write a generator (function), genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

# Hints
# Ideas about the problem

# Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.

class theClass(object):
    """docstring for theClass."""
    def __init__(self, arg):
        super(theClass, self).__init__()
        self.arg = arg

for i in range(10):
    print(i)
