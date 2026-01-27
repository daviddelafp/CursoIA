import random
import statistics

# ============================================================
# CONFIGURACIÓN GLOBAL DEL ALGORITMO GENÉTICO
# ============================================================

# Semilla para reproducibilidad
# Tamaño de la población
NUM_GENERACIONES = 0            # Número de generaciones
# Número de individuos élite
# Tamaño del torneo
# Probabilidad de mutación POR GEN

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

    return poblacion

# ============================================================
# FUNCIÓN DE FITNESS
# ============================================================

def calcular_fitness(individuo):
    """
    Calcula qué tan bueno es un individuo
    Cuanto menor sea el fitness, mejor es la solución
    """
    # IMPLEMENTAR
    pass

# ============================================================
# SELECCIÓN POR TORNEO
# ============================================================

def seleccion_por_torneo(poblacion):
    """
    Selecciona un individuo usando torneo de tamaño K
    """
    # IMPLEMENTAR
    pass

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
    pass

# ============================================================
# BUCLE PRINCIPAL DEL ALGORITMO GENÉTICO
# ============================================================

def algoritmo_genetico():

    poblacion = crear_poblacion_inicial()

    for generacion in range(NUM_GENERACIONES):

        # ====================================================
        # AQUÍ VA EL CÁLCULO DE FITNESS DE TODA LA POBLACIÓN
        # ====================================================

        nueva_poblacion = []

        # ====================================================
        # AQUÍ VA EL ELITISMO
        # PARA ELLO, PODRÍAS ORDENAR LA POBLACIÓN SEGÚN FITNESS
        # ====================================================

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
