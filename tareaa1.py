# 1. Validador de notas con promedio
# Paso 1 — Entender el problema (EPS)
# Entrada: Notas sueltas o en lote, algunas fuera de rango.
# Proceso: Validar cada nota una por una; si es válida, agregarla a la lista interna; al final, sumar y dividir entre la cantidad para el promedio.
# Salida: Lista de notas válidas y el promedio de esas notas.
# Paso 2 - Bosquejo a mano
# Datos: 85, 92, 110, -5, 78, 88
# ¿85 es válida?   0 ≤ 85 ≤ 100  -> SÍ  -> lista = [85]
# ¿92 es válida?   0 ≤ 92 ≤ 100  -> SÍ  -> lista = [85, 92]
# ¿110 es válida?  0 ≤ 110 ≤ 100 -> NO  -> se descarta
# ¿-5 es válida?   0 ≤ -5 ≤ 100  -> NO  -> se descarta
# ¿78 es válida?   0 ≤ 78 ≤ 100  -> SÍ  -> lista = [85, 92, 78]
# ¿88 es válida?   0 ≤ 88 ≤ 100  -> SÍ  -> lista = [85, 92, 78, 88]
#promedio = (85+92+78+88) / 4 = 343 / 4 = 85.75
# Paso 3 - Descubrir el patron
# Lo que se repite: la validación (0 ≤ nota ≤ 100) es siempre la misma prueba, por eso vive en su propio método validar_nota.
# Lo que cambia: la cantidad de notas que llegan de una sola vez — por eso cargar_notas usa *args y llama a validar_nota una vez por cada elemento, en lugar de repetir el if muchas veces.
# Paso 4 - Codigo
class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self,nota):
        if nota >=0 and nota <= 100:
            return True
        else:
            return False
        #return 0 <= nota <= 100
    
    def cargar_notas(self,*args):
        
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(-60,80,40,200))
print(cal.promedio())
# Paso 5 - Prueba de escritorio
# Acción	                         self.notas	             Salida
# c = Calificador()	                 []	                     —
# cargar_notas(85,92,110,78,-5,88)	 [85, 92, 78, 88]	     [85, 92, 78, 88]
# promedio()	                     [85, 92, 78, 88]	     85.75

# 2. Contador de palabras unicas
# Paso 1 - Entender el problema (EPS)
# Entrada: Palabras sueltas o en lote, algunas repetidas.
# Proceso: Cada palabra se agrega a un conjunto (elimina duplicados automáticamente) y a una lista (conserva el orden de llegada).
# Salida: Cantidad de palabras únicas.
# Paso 2 - Bosquejo a mano
# Datos: "hola", "mundo", "hola"
# agregar_palabra("hola")  -> conjunto = {"hola"}          lista = ["hola"]
# agregar_palabra("mundo") -> conjunto = {"hola","mundo"}  lista = ["hola","mundo"]
# agregar_palabra("hola")  -> conjunto sigue igual (ya estaba) lista = ["hola","mundo","hola"]
# contar_palabras() = len(conjunto) = 2
# Paso 3 - Descubrir el patron 
# Lo que se repite: la acción de "guardar una palabra" es siempre la misma, por eso agregar_multiples no reescribe la lógica, solo hace un bucle que llama a agregar_palabra.
# Lo que cambia: cuántas palabras llegan de una vez. El conjunto resuelve la unicidad; la lista resuelve el orden — son dos colecciones para dos necesidades distintas sobre el mismo dato.
# Paso 4 - Codigo

class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        self.unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabra(self):
        return len(self.unicas)
    
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola", "mundo", "como estas")
print(f"Palabras unicas: {at.contar_palabra()}")
print(f"Orden de llegada: {at.orden}")
# Paso 5 — Prueba de escritorio
# Acción	                                     self.unicas	     self.orden
# at = AnalizadorTexto()	                     set()	             []
# agregar_multiples("hola","mundo","hola")	     {"hola","mundo"}	 ["hola","mundo","hola"]
# contar_palabras()	                             {"hola","mundo"}	 → 2

# 3. Gestor de compras con totales
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombre y precio de cada artículo.
# Proceso: Guardar cada par nombre→precio en un diccionario; sumar los valores para el total; filtrar por rango de precio recorriendo items().
# Salida: Total del carrito y lista de artículos filtrados.
# Paso 2 - Bosquejo a mano
# agregar_articulo("pan", 2.50)   -> dict = {"pan": 2.50}
# agregar_articulo("leche", 3.00) -> dict = {"pan": 2.50, "leche": 3.00}
# total_carrito() = 2.50 + 3.00 = 5.50
# articulos_por_rango(2.00, 3.00):
# "pan"   -> 2.50 está en [2.00, 3.00] -> SÍ
# "leche" -> 3.00 está en [2.00, 3.00] -> SÍ
# -> ["pan", "leche"]
# Paso 3 - Descubrir el patron 
# El diccionario es el "almacén" natural cuando cada dato tiene una clave única 
# (el nombre del artículo) asociada a un valor (el precio). 
# total_carrito y articulos_por_rango no repiten la lógica de guardado: 
# solo leen lo que ya está en self.articulos de dos formas distintas (sumar vs. filtrar).
# Paso 4 - Codigo
class CarroCompras():
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    
    def total_carrito(self):
        return sum(self.articulos.values())
    
    def articulos_por_rango(self, precio_min, precio_max):
        return [nombre for nombre, precio in self.articulos.items()
                if precio_min <= precio <= precio_max]

c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
print(f"Total: {c.total_carrito()}")
print(f"Entre 2.00 y 3.00: {c.articulos_por_rango(2.00, 3.00)}")
# Paso 5 _ Prueba de escritorio 
# Acción	                        self.articulos	                 Salida
# c = CarroCompras()	            {}	                             —
# agregar_articulo("pan",2.50)	    {"pan": 2.50}	                 —
# agregar_articulo("leche",3.00)	{"pan": 2.50, "leche": 3.00}	 —
# total_carrito()	                {"pan": 2.50, "leche": 3.00}	 5.50

# 4. Inversor de secuencias
# Paso 1 - Entender el problema (EPS)
# Entrada: Una lista, o varias listas a la vez.
# Proceso: Recorrer la lista de atrás hacia adelante con un índice manual, construyendo una lista nueva; para varias listas, repetir el proceso y guardar cada resultado en un diccionario (usando tuplas como clave, porque una lista no puede ser clave de diccionario).
# Salida: Lista invertida, o diccionario con varias listas invertidas.
# Paso 2 — Bosquejo a mano
# Datos: [1, 2, 3]   (largo = 3, índices válidos 0,1,2)
# i = 2 -> lista[2] = 3 -> invertida = [3]
# i = 1 -> lista[1] = 2 -> invertida = [3, 2]
# i = 0 -> lista[0] = 1 -> invertida = [3, 2, 1]
# Resultado: [3, 2, 1] 
# Paso 3 — Descubrir el patrón
# Lo que se repite: recorrer una lista de atrás hacia adelante siempre usa el mismo truco de índices (range(len(lista)-1, -1, -1)). 
# Lo que cambia: cuántas listas llegan; invertir_multiples no vuelve a escribir el bucle de inversión, solo llama a invertir_lista una vez por cada lista recibida.
# Paso 4 - Codigo
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado

inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(inv.invertir_multiples([1, 2, 3], [4, 5]))
# Paso 5 — Prueba de escritorio
# i	   lista[i]	  invertida
# 2	   3	      [3]
# 1	   2	      [3, 2]
# 0	   1	      [3, 2, 1]

# 5. Detector de números pares e impares
# Paso 1 - Entender el problema (EPS) 
# Entrada: Varios números en un solo lote.
# Proceso: Para cada número, preguntar si es par con el operador %; según la respuesta, agregarlo a la lista correspondiente dentro del diccionario.
# Salida: Diccionario clasificado y tupla con las cantidades.
# Paso 2 - Bosquejo a mano
# Paso 2 — Bosquejo a mano
# Datos: 1, 2, 3, 4, 5
# 1 % 2 = 1 -> impar -> impares=[1]
# 2 % 2 = 0 -> par   -> pares=[2]
# 3 % 2 = 1 -> impar -> impares=[1,3]
# 4 % 2 = 0 -> par   -> pares=[2,4]
# 5 % 2 = 1 -> impar -> impares=[1,3,5]
# Resultado: {'pares':[2,4], 'impares':[1,3,5]}
# cantidad_pares_impares() = (2, 3)
# Paso 3 - Buscar el patron 
# es_par encapsula la única pregunta que se repite (numero % 2 == 0); separar no vuelve a escribir esa condición, solo la usa dentro de un if/else para decidir en qué lista del diccionario cae cada número. 
# Guardar el último resultado en un atributo permite que cantidad_pares_impares no tenga que recibir los números de nuevo.
# Paso 4 - Codigo
class AnalizadorNumeros:
    def __init__(self):
        self.ultimo_resultado = {'pares': [], 'impares': []}

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        resultado = {'pares': [], 'impares': []}
        for numero in numeros:
            if self.es_par(numero):
                resultado['pares'].append(numero)
            else:
                resultado['impares'].append(numero)
        self.ultimo_resultado = resultado
        return resultado

    def cantidad_pares_impares(self):
        return (len(self.ultimo_resultado['pares']),
                len(self.ultimo_resultado['impares']))

an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())
# Paso 5 - Prueba de escritorio
# Número	es_par()	pares	impares
# 1	False	[]	[1]
# 2	True	[2]	[1]
# 3	False	[2]	[1, 3]
# 4	True	[2, 4]	[1, 3]
# 5	False	[2, 4]	[1, 3, 5]