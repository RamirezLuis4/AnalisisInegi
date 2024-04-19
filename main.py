import pandas as pd
import utils.correlation_calculator as cc
import utils.AnalisisTendenciasNatalidad as at

# Cargar el conjunto de datos de natalidad
dataset_path = "data/conjunto_de_datos_natalidad_2022.txt"
natalidad_data = pd.read_csv(dataset_path)

# Seleccionar las variables de interés
variable1 = "edad_madn"
variable2 = "edad_reg"

# Calcular la correlación entre las dos variables
correlacion = cc.calcular_correlacion_entre_variables(natalidad_data, variable1, variable2)

# Muestra la correlación
print(f"Correlación entre {variable1} y {variable2}: {correlacion}")

# Seleccionar las variables de interés
variable_tiempo = "ano_nac"
variable_nacimientos = "hijos_vivo"


# Llamar a la función para analizar las tendencias de natalidad
at.analisis_tendencias_natalidad(natalidad_data, variable_tiempo, variable_nacimientos)





