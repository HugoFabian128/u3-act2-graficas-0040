import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Marcas de Automóviles
# Hugo Fabian NC 0040 - Problema 4: Autos
toy = ['Toyota', 'Japón', True, 1937]
tsl = ['Tesla', 'EEUU', True, 2003]
bmw = ['BMW', 'Alemania', True, 1916]
ford = ['Ford', 'EEUU', True, 1903]
fer = ['Ferrari', 'Italia', True, 1939]

lista_autos = [toy, tsl, bmw, ford, fer]
df_autos = pd.DataFrame(lista_autos, columns=("Marca", "Pais_Origen", "Fabrica_Electricos", "Año_Fundacion"))

# 1. Gráfica de líneas
plt.plot(df_autos["Marca"], df_autos["Año_Fundacion"])
plt.title("Fundación de autos 0040")
plt.xlabel("Marca")
plt.ylabel("Año de fundación")
plt.show()

# 2. Gráfica de dispersión
plt.scatter(df_autos["Marca"], df_autos["Año_Fundacion"])
plt.title("Dispersión: Marcas vs Año")
plt.xlabel("Marca")
plt.ylabel("Año de fundación")
plt.show()

# 3. Gráfica de barras
plt.bar(df_autos["Marca"], df_autos["Año_Fundacion"])
plt.title("Año de fundación por marca 0040")
plt.xlabel("Marca")
plt.ylabel("Año de fundación")
plt.show()

# 4. Gráfica de barras (Orden descendente y con colores)
df_autos_ordenar = df_autos.sort_values("Año_Fundacion", ascending=False)
plt.bar(df_autos_ordenar["Marca"], df_autos_ordenar["Año_Fundacion"], color=["b", "g", "c", "m", "y"])
plt.title("Marcas ordenadas por año 0040")
plt.xlabel("Marca")
plt.ylabel("Año de fundación")
plt.show()

# 5. Gráfica de pastel
plt.pie(df_autos["Año_Fundacion"], labels=df_autos["Marca"])
plt.title("Distribución por año 0040")
plt.show()