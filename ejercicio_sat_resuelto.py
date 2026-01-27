from pysat.formula import CNF
from pysat.solvers import Solver

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
HORAS = [0, 1]  # 0 = primera hora, 1 = segunda hora

ASIGNATURAS = [
    "Cálculo",
    "Física",
    "Álgebra",
    "Programación",
    "Búsqueda"
]

# 50 variables, una por cada combinación de asignatura, día y hora. 
# Cada una de ellas puede ser verdadera o false
def var(dia, hora, asignatura):
    return (DIAS.index(dia) * len(HORAS) * len(ASIGNATURAS)) + \
           (hora * len(ASIGNATURAS)) + \
           ASIGNATURAS.index(asignatura) + 1

cnf = CNF()

# ============================================================
# REGLA 1: Cada hueco horario tiene EXACTAMENTE una asignatura
# BÁSICAMENTE, NO PUEDE HABER DOS ASIGNATURAS A LA VEZ A LA MISMA HORA. 
# ADEMÁS, DEBE HABER AL MENOS UNA ASIGNATURA IMPARTIÉNDOSE A CADA HORA CADA DÍA
# EN DEFINITIVA, DEL TOTAL DE VARIABLES (50), SOLO 10 DEBEN SER TRUE. 
# ============================================================

for dia in DIAS:
    for hora in HORAS:
        variables = [var(dia, hora, a) for a in ASIGNATURAS]

        cnf.append(variables)  # al menos 1 asignatura impartiéndose ese día a esa hora

        for i in range(len(variables)):
            for j in range(i + 1, len(variables)):
                # Dado un día y una hora, solo puede haber una asignatura siendo impartida en ese momento, no dos a la vez. 
                # Si dos se imparten a la vez el mismo día a la misma hora: not True or not True = False. MAL.
                cnf.append([-variables[i], -variables[j]])  

# ============================================================
# REGLA 2 + REGLA 4:
# EXACTAMENTE una clase a PRIMERA hora y EXACTAMENTE una a SEGUNDA por asignatura
# ============================================================

for asignatura in ASIGNATURAS:

    # Primera hora → exactamente 1 día. Es decir, cada asignatura se imparte un día a primera. 
    # Aunándolo con la regla 1 que decía que solo puede haber una asignatura a la vez, no ...
    # ... sería necesario indicar que no puede haber dos días de la semana distintos con la misma ...
    # ... asignatura a primera, por lo que el bucle de abajo sobra y ha sido comentado.  
    primera = [var(d, 0, asignatura) for d in DIAS]
    cnf.append(primera)

    '''
    for i in range(len(primera)):
        for j in range(i + 1, len(primera)):
            cnf.append([-primera[i], -primera[j]])
    '''

    # Segunda hora → exactamente 1 día. Es decir, cada asignatura se imparte un día a segunda hora. 
    # Aunándolo con la regla de arriba que decía que solo puede haber una asignatura a la vez, no ...
    # ... sería necesario indicar que no puede haber dos días de la semana distintos con la misma ...
    # ... asignatura a primera, por lo que el bucle de abajo sobra y ha sido comentado.  
    segunda = [var(d, 1, asignatura) for d in DIAS]
    cnf.append(segunda)

    '''
    for i in range(len(segunda)):
        for j in range(i + 1, len(segunda)):
            cnf.append([-segunda[i], -segunda[j]])
    '''

# ============================================================
# REGLA 3: No repetir asignatura el mismo día
# ============================================================

for dia in DIAS:
    for asignatura in ASIGNATURAS:
        # Si para una asignatura y día, tanto para primera y segunda hora son True, not True or not True = False. 
        cnf.append([-var(dia, 0, asignatura), -var(dia, 1, asignatura)])

# ============================================================
# REGLA 5: Física NO miércoles
# ============================================================

for hora in HORAS:
    # Tanto para primera como para segunda hora. 
    cnf.append([-var("Miércoles", hora, "Física")])

# ============================================================
# REGLA 6: Álgebra NO lunes, martes, miércoles a segunda
# ============================================================

for dia in ["Lunes", "Martes", "Miércoles"]:
    cnf.append([-var(dia, 1, "Álgebra")])

# ============================================================
# REGLA 7: Cálculo y Programación NO seguidas
# ============================================================

for dia in DIAS:
    # Si ambas son True el mismo día (da igual el orden), Not True or Not True = False
    cnf.append([-var(dia, 0, "Cálculo"), -var(dia, 1, "Programación")])
    cnf.append([-var(dia, 0, "Programación"), -var(dia, 1, "Cálculo")])

# ============================================================
# REGLA 8: Búsqueda Viernes SEGUNDA
# ============================================================

cnf.append([var("Viernes", 1, "Búsqueda")])

# ============================================================
# REGLA 9: Física y Búsqueda NO seguidas
# ============================================================

for dia in DIAS:
    # Similar a la regla 7. 
    cnf.append([-var(dia, 0, "Física"), -var(dia, 1, "Búsqueda")])
    cnf.append([-var(dia, 0, "Búsqueda"), -var(dia, 1, "Física")])

# ============================================================
# REGLA 10: Programación Lunes PRIMERA
# ============================================================

cnf.append([var("Lunes", 0, "Programación")])
# print(len(cnf.clauses)) # Numero de clausulas. 


# ============================================================
# MOSTRAR SOLUCIONES
# ============================================================

def mostrar_horario(modelo):
    '''Una función para imprimirlo bonito, básicamente'''
    horario = {dia: ["", ""] for dia in DIAS}

    for lit in modelo:
        if lit > 0:
            lit -= 1
            asignatura = ASIGNATURAS[lit % len(ASIGNATURAS)]
            hora = (lit // len(ASIGNATURAS)) % len(HORAS)
            dia = DIAS[(lit // (len(HORAS) * len(ASIGNATURAS)))]

            horario[dia][hora] = asignatura

    print("Horario encontrado:")
    for dia in DIAS:
        print(f"{dia}: {horario[dia][0]}  |  {horario[dia][1]}")
    print("-" * 50)

# ============================================================
# ENUMERAR TODAS LAS SOLUCIONES
# ============================================================

soluciones = 0

with Solver(bootstrap_with=cnf) as solver:
    while solver.solve():
        modelo = solver.get_model()
        mostrar_horario(modelo)

        # Cuando se encuentra una solución, incrementamos en uno el contador de soluciones ...
        # ... y añadimos una cláusula que nos diga que esa combinación solución de Trues y Falses ...
        # ... no debe darse, para que al volver a llamar al solver de SAT nos de una respuesta diferente. 
        soluciones += 1
        solver.add_clause([-lit for lit in modelo])

print(f"Total de soluciones encontradas: {soluciones}")
