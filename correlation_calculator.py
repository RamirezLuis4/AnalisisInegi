import seaborn as sns
import matplotlib.pyplot as plt
def calcular_correlacion_entre_variables(dataset, variable1, variable2):
    # Calcula el coeficiente de correlación
    correlation = dataset[variable1].corr(dataset[variable2])

    # Crea una gráfica de dispersión
    sns.scatterplot(data=dataset, x=variable1, y=variable2)

    # Añade el título y etiquetas de los ejes
    plt.title(f"Correlación entre {variable1} y {variable2}: {correlation:.2f}")
    plt.xlabel(variable1)
    plt.ylabel(variable2)

    # Muestra la gráfica
    plt.show()

    return correlation