#################################
# CREADOR DE HISTOGRAMAS NORMALES#
#################################

# CARGAR LIBRERIAS
import numpy as np
import pandas as pd
import argparse

# Crear un "Parser"
parser = argparse.ArgumentParser(
    description="Programa para genear histogramas normales")
parser.add_argument("media", help="Promedio de la distribucion")
parser.add_argument("desv", help="Error de la distribucion")
# Opcional para el usuario
parser.add_argument("--n", default=100, help="Numero de datos a generar")

args = parser.parse_args()

# DEFINIR VARIABLES
n = int(args.n)
media = float(args.media)
desv = float(args.desv)

# GENERAR NUMEROS ALEATORIOS
datos = np.random.normal(size=n, loc=media, scale=desv)

# TRANSFORMAR LOS NUMEROS ALEATORIOS EN GENERADOS EN ENTEROS
datos = datos.round(0).astype(int)

# QUITAR COLAS DE LA DISTRIBUCION (QUITAR VALORES ATIPICOS)
datos_trim = []
for i in range(len(datos)):
    if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv:
        datos_trim.append(datos[i])

# COSNTRUIR DATAFRAME CON LOS DATOS TRUNCADOS
datos_trim = pd.DataFrame(datos_trim)
datos_trim.columns = ['Datos']

# CONTAR (FRECUENCIA) DE CADA UNO DE LOS CASOS GENERADOS
histograma = datos_trim.groupby('Datos').size()


for i in range(len(histograma)):

    # ASIGNAR "+" SI CADA DATO GENERADO ES POSITIVO
    if histograma.index[i] >= 0:
        s = "+"
    else:
        s = ""

    # IMPRIMIR CADA DATO GENERADO, UN ESPACIO Y LUEGO UNA CANTIDAD DE ASTERISCOS
    # QUE DEPENDE DE LA PROPORCION DE VECES QUE SE OBSERVO ESE DATO
    print(
        s,
        histograma.index[i],
        ' '*(1+len(str(np.max([np.max(histograma.index),
                               abs(np.min(histograma.index))]))) -
             len(str(abs(histograma.index[i])))),
        '*'*round(100*histograma.iloc[i]/len(datos_trim)),
        sep=""
    )
