# Lista de frutas en plural y singular
fruits_plural = [
   "naranjas", "mandarinas", "toronjas", "fresas", "guayabas", "limones",
   "piñas", "mangos", "papayas", "melones", "sandias", "ciruelas",
   "duraznos", "higos", "peras", "tunas", "manzanas", "uvas", "granadas"
           ]
        
fruits_singular = [
    "naranja", "mandarina", "toronja", "fresa", "guayaba","limon",
    "piña", "mango", "papaya", "melon", "sandia", "ciruela",
    "durazno", "higo", "pera", "tuna", "manzana", "uva","granada"
                            ]

#diccionario para transformar de pluaral a singular
mapping_plural_to_singular = {
            "naranjas": "Naranja",
            "mandarinas": "Mandarina",
            "toronjas": "Toronja",
            "fresas": "Fresa",
            "guayabas": "Guayaba",
            "limones": "Limon",
            "piñas": "Piña",
            "mangos": "Mango",
            "papayas": "Papaya",
            "melones": "Melon",
            "sandias": "Sandia",
            "ciruelas": "Ciruela",
            "duraznos": "Durazno",
            "higos": "Higo",
            "peras": "Pera",
            "tunas": "Tuna",
            "manzanas": "Manzana",
            "uvas": "Uva",
            "granadas": "Granada",
        }

dict_precios = {
    "Naranja": 15,
    "Mandarina": 20,
    "Toronja": 25,
    "Fresa": 60,
    "Guayaba": 35,
    "Limon": 20,
    "Piña": 30,
    "Mango": 35,
    "Papaya": 20,
    "Melón": 30,
    "Sandía": 15,
    "Ciruela": 45,
    "Durazno": 50,
    "Higo": 70,
    "Pera": 40,
    "Tuna": 20,
    "Manzana": 35,
    "Uva": 60,
    "Granada": 80
}


# Este metodo se le envia un texto y si se encuentra dentro de la lista de frutas retorna el nombre de la fruta en singular
# Este ignora plurales y retorna el nombre en singular
def detectarFruta(texto):
  # quitar acentos
  texto = normalize(texto)

  if texto in fruits_singular :
    return texto
  elif texto in fruits_plural :
    # si esta en plural normalizar a ser en singular
    return mapping_plural_to_singular.get(texto)
  else:
    # no esta en la lista de frutas
    print(texto)
    return False
  

# funcion para calcular costo de cada fruta
# recibe el nombre de la fruta y la cantidad y retorna el costo de el resultado
def calcularCosto(fruta, cantidad):
   if fruta in dict_precios:
      print("Fruta: ", fruta, "Cantidad: ", cantidad, "total", dict_precios.get(fruta) * cantidad)
      return dict_precios.get(fruta) * cantidad
      
   else:
      return 0
   

#funcion para crear factura
def crearFactura(datos, nombre):
  factura = {}

  #agregar nombre
  factura["facturar_a"] = nombre

  #calcular costo singular y total
  total = 0
  factura["items"] = []
  for fruta, cantidad in datos.items():
    costo = calcularCosto(fruta, cantidad)
    total += costo
    factura["items"].append({
      "cantidad": cantidad,
      "descripcion": fruta,
      "precio_unitario": dict_precios.get(fruta),
      "importe": costo
    })

  factura["subtotal"] = total
  
  return factura

# funcion para eliminar acentos
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

# de https://micro.recursospython.com/recursos/como-quitar-tildes-de-una-cadena.html