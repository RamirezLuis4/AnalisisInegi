import matplotlib.pyplot as plt

def analisis_tendencias_natalidad(data, variable_tiempo, variable_nacimientos):
    # Filtrar los datos para incluir solo los años 2000-2022
    data_filtrado = data[(data[variable_tiempo] >= 2000) & (data[variable_tiempo] <= 2022)]

    # Agrupar los datos por la variable de tiempo y sumar el número de nacimientos
    tendencias = data_filtrado.groupby(variable_tiempo)[variable_nacimientos].sum()

    # Crear una figura y un eje
    fig, ax = plt.subplots(figsize=(10, 6))

    # Graficar las tendencias de natalidad a lo largo del tiempo
    ax.plot(tendencias.index, tendencias.values, marker='o', linestyle='-')

    # Configurar etiquetas y título
    ax.set_xlabel('Año de nacimiento')
    ax.set_ylabel('Número de nacimientos')
    ax.set_title('Tendencias de natalidad a lo largo del tiempo')

    # Limitar los ejes x e y para mostrar solo los años 2000-2022
    plt.xlim(2000, 2022)

    # Mostrar la gráfica
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()