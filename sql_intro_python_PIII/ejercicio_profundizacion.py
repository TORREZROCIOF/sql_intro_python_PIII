import sqlite3
import numpy as np
import matplotlib.pyplot as plt

# Función fetch para leer los datos de la base de datos
def fetch(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT pulso FROM sensor")
    rows = cursor.fetchall()
    data = [row[0] for row in rows]
    conexion.close()

    return data

# Función show para graficar los datos
def show(data):
    fig = plt.figure()
    fig.suptitle('Evolución del Ritmo Cardíaco Durante el Partido', fontsize=16)
    ax = fig.add_subplot()
    ax.plot(data, c='darkgreen', label='Pulso')
    ax.legend()
    ax.grid()
    plt.xlabel('Tiempo')
    plt.ylabel('Pulso')
    plt.show()

# Función estadistica para calcular e imprimir estadísticas básicas
def estadistica(data):
    media = np.mean(data)
    minimo = np.min(data)
    maximo = np.max(data)
    estandar = np.std(data)

    print(f"Valor Medio : {media}")
    print(f"Valor Mínimo : {minimo}")
    print(f"Valor Máximo : {maximo}")
    print(f"Desvío Estándar : {estandar}")

# Función regiones para dividir y graficar los datos por zonas de interés
def regiones(data):
    # Calcular la media y el desvío estándar
    media = np.mean(data)
    estandar = np.std(data)

    # Listas para almacenar los índices (x) y los valores de pulso (y)
    # Valores tranquilos (pulso <= media - estandar)
    x1 = []
    y1 = []
    # Valores muy emocionados (pulso >= media + estandar)
    x2 = []
    y2 = []
    # Valores normales (entre media - estandar y media + estandar)
    x3 = []
    y3 = []

    # Clasificar los datos en las diferentes regiones
    for i in range(len(data)):
        if data[i] <= media - estandar:
            x1.append(i)
            y1.append(data[i])
        elif data[i] >= media + estandar:
            x2.append(i)
            y2.append(data[i])
        else:
            x3.append(i)
            y3.append(data[i])

    fig = plt.figure()
    fig.suptitle('Zonas de Ritmo Cardíaco Durante el Partido', fontsize=16)
    ax1 = fig.add_subplot(1, 3, 1)  
    ax2 = fig.add_subplot(1, 3, 2)  
    ax3 = fig.add_subplot(1, 3, 3)  

    ax1.plot(x1, y1,color='blue', label='Tranquilo',alpha=0.5)
    ax1.legend()
    ax1.grid()

    ax2.plot(x2, y2, color='red', label='Emocionado',alpha=0.5)
    ax2.legend()
    ax2.grid()

    ax3.plot(x2, y2, color='green', label='Normal')
    ax3.legend()
    ax3.grid()

    plt.show()
    print("Fin scatter plot")



# Flujo principal del programa
if __name__ == "__main__":

    conexion = sqlite3.connect('heart.db')
    # Leer la base de datos
    data = fetch(conexion)

    # Mostrar la evolución del pulso cardíaco
    show(data)

     # Imprimir estadísticas
    estadistica(data)

    # Graficar las diferentes regiones de interés
    regiones(data)