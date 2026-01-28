import random
import statistics

# ============================================================
# CONFIGURACIÓN GLOBAL DEL ALGORITMO GENÉTICO
# ============================================================

random.seed(42)                 # Semilla para reproducibilidad
TAM_POBLACION = 100             # Tamaño de la población
NUM_GENERACIONES = 10           # Número de generaciones
NUM_ELITE = 4                   # Número de individuos élite
K = 3                           # Tamaño del torneo
PROB_MUTACION = 0.01            # Probabilidad de mutación POR GEN

# ============================================================
# DEFINICIÓN DEL PROBLEMA
# ============================================================

NUM_MAQUINAS = 10

# Lista con los minutos que tarda cada tarea
# (50 tareas en total)
TIEMPOS_TAREAS = [
    120, 90, 60, 30, 200, 45, 70, 80, 55, 100,
    95, 65, 85, 110, 130, 150, 40, 50, 75, 105,
    115, 140, 160, 35, 25, 20, 180, 190, 210, 220,
    10, 15, 95, 100, 135, 145, 155, 165, 175, 185,
    195, 205, 215, 225, 235, 240, 250, 260, 270, 280
]

NUM_TAREAS = len(TIEMPOS_TAREAS)

# ============================================================
# FUNCIÓN PARA CREAR UN INDIVIDUO ALEATORIO
# ============================================================

def crear_individuo_aleatorio():
    """
    Crea un individuo aleatorio
    """
    individuo = []

    # IMPLEMENTAR
    for _ in range(NUM_TAREAS):
        individuo.append(random.randint(0,NUM_MAQUINAS-1))

    return individuo

# ============================================================
# CREACIÓN DE LA POBLACIÓN INICIAL
# ============================================================

def crear_poblacion_inicial():
    """
    Crea la población inicial aleatoria
    """
    poblacion = []

    # IMPLEMENTAR
    # Debe crearse llamando a crear_individuo_aleatorio()
    
    for _ in range(TAM_POBLACION):
        poblacion.append(crear_individuo_aleatorio())

    return poblacion

# ============================================================
# FUNCIÓN DE FITNESS
# ============================================================

def calcular_fitness(individuo):
    """
    Calcula qué tan bueno es un individuo
    Cuanto menor sea el fitness,  mejor es la solución
    """
    # IMPLEMENTAR
     
    tiempos_maquinas = [0] * NUM_MAQUINAS
    for tarea, maquina in enumerate(individuo):
        tiempos_maquinas[maquina] += TIEMPOS_TAREAS[tarea]

    n = len(tiempos_maquinas)           #media Numero de maquinas
    media = sum(tiempos_maquinas) / n   #media Total de tiempo entre numero de maquinas

    suma = 0.0                      #acumulador para varianza
    for tiempo in tiempos_maquinas: #recorrer el tiempo de cada maquina
        diff = tiempo - media       #diferencia entre el tiempo de la maquina y la media
        suma += diff * diff         #sumar el cuadrado de la diferencia para positivos y negativos
    varianza = suma / n             #media de las sumas por el numero de maquinas

    fitness = varianza ** 0.5       # Desviación estándar

    return fitness # fitness_cada_individuo[tuple(individuo)]




# ============================================================
# SELECCIÓN POR TORNEO
# ============================================================

def seleccion_por_torneo(poblacion):
    """
    Selecciona un individuo usando torneo de tamaño K
    """
    # IMPLEMENTAR
    torneo = random.sample(poblacion, K)
    mejor_individuo = min(torneo, key=lambda ind: calcular_fitness(ind))

    return mejor_individuo
    

# ============================================================
# CRUCE ENTRE DOS PADRES
# ============================================================

def cruce(padre1, padre2):
    """
    Realiza cruce entre dos padres y devuelve dos hijos
    """

    hijo1 = None
    hijo2 = None

    # IMPLEMENTAR

    return hijo1, hijo2

# ============================================================
# MUTACIÓN POR GEN
# ============================================================

def mutar(individuo):
    """
    Aplica mutación gen a gen según PROB_MUTACION
    """

    # IMPLEMENTAR

    pass

# ============================================================
# FUNCIÓN PARA IMPRIMIR LOS MEJORES FITNESS
# ============================================================

def imprimir_mejores_fitness(fitness_cada_individuo, generacion):
    lista=[]

    for individuos in fitness_cada_individuo:
        lista.append(fitness_cada_individuo[individuo])
    
    lista.sort()

    print(f"Mejores 10 fitness de generación numero {generacion}:")

    for fitness in lista [:10]:
        print(fitness)
    
    print("\n")

# ============================================================
# BUCLE PRINCIPAL DEL ALGORITMO GENÉTICO
# ============================================================

def algoritmo_genetico():

    poblacion = crear_poblacion_inicial()
    #print(len(poblacion))

    for generacion in range(NUM_GENERACIONES):

        # ====================================================
        # AQUÍ VA EL CÁLCULO DE FITNESS DE TODA LA POBLACIÓN
        # ====================================================
        fitness_cada_individuo = {}
        for individuo in poblacion:
            fitness_cada_individuo[tuple(individuo)] = calcular_fitness(individuo)
            #print(fitness_cada_individuo)
            #exit()

        nueva_poblacion = []

        # ====================================================
        # AQUÍ VA EL ELITISMO
        # PARA ELLO, PODRÍAS ORDENAR LA POBLACIÓN SEGÚN FITNESS
        # ====================================================
        poblacion_ordenada = sorted(poblacion, key=lambda ind: fitness_cada_individuo[tuple(ind)])
        nueva_poblacion.append(poblacion_ordenada[:NUM_ELITE])
        #print(nueva_poblacion)   #hasta aqui bien
        #exit()
        # ====================================================
        # AQUÍ VA LA SELECCIÓN DE PADRES
        # ====================================================

        

        # ====================================================
        # AQUÍ VA EL CRUCE PARA GENERAR HIJOS
        # ====================================================

        # ====================================================
        # AQUÍ VA LA MUTACIÓN DE LOS HIJOS
        # ====================================================

        # ====================================================
        # AQUÍ VA EL REEMPLAZO DE LA POBLACIÓN
        # ====================================================

        # ====================================================
        # IMPRIMIR LOS MEJORES FITNESS DE LA GENERACIÓN
        # ====================================================

        # ====================================================
        # REINICIAR EL DICCIONARIO DE FITNESS AL FINAL
        # OTRA ALTERNATIVA ES REINICIAR ESTO AL INICIO DEL BUCLE
        # DE ESTA FORMA, ES MÁS SENCILLO IMPRIMIR EL MEJOR INDIVIDUO FINAL
        # ====================================================

    # ========================================================
    # AQUÍ VA LA IMPRESIÓN DEL MEJOR INDIVIDUO FINAL
    # ========================================================

if __name__ == "__main__":
    algoritmo_genetico()
