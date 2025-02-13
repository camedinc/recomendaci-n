# -*- coding: utf-8 -*-
"""funciones.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vOaASlWKrjPxLF3ET8ws3C0vUBXFJuZV
"""

# Función que recibe un usuario, tabla de recomendaciones y retorna las primeras n
def recomendaciones_usuario(user, predicciones, n):
  predicciones = predicciones[predicciones['uid'] == user] # filtra recomencaaciones por usuario
  predicciones = predicciones.sort_values(by = 'est', ascending = False)  # ordena recomendaciones de mayor a menor valoración
  predicciones = predicciones.head(n) # retorna las n
  return predicciones