ConversionMeses = {
  "Ene": "Enero",
  "Feb": "Febrero",
  "Mar": "Marzo",
  "Abr": "Abril",
  "May": "Mayo",
  "Jun": "Junio",
  "Jul": "Julio",
  "Ago": "Agosto",
  "Sep": "Septiembre",
  "Oct": "Octubre",
  "Nov": "Noviembre",
  "Dic": "Diciembre",
}

print(ConversionMeses["Nov"])
#imprime "Noviembre"

print(ConversionMeses.get("Dic"))
#imprime "Diciembre"

print(ConversionMeses.get("fjfj"))
#imprime "none"

#Definir resultado de una key que no pertenece
#al diccionario
print(ConversionMeses.get("jeje","No es valido"))
#imprime "No es valido"
