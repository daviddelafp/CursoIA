from unified_planning.io import PDDLReader
from unified_planning.shortcuts import OneshotPlanner

reader = PDDLReader()
problem = reader.parse_problem("domain_bloques.pddl", "problem_bloques.pddl")

'''
Esto de abajo es "lo mismo" que hacer: 
planner = OneshotPlanner(name="fast-downward")
result = planner.solve(problem)

Pero por si acaso se queda algo sin cerrar cuando termine el planificador se hace con el with
'''
with OneshotPlanner(name="pyperplan") as planner:
    result = planner.solve(problem)
    # Por defecto usa el algoritmo greedy del mejor primero. 
    # Por defecto usa la heurística FF (hFF). Tamaño de un plan relajado subóptimo. No es admisible. 

'''
Si se quiere la solución óptima usar el planner fast-downward y A* con hmax. En windows fast-downward es difícil de hacerlo funcionar.  
Pyperplan no soporta hmax(). El planificador no está pensado para trabajar con esta heurística. 
hmax: heurística admisible. Parte del coste de la solución del plan del dominio relajado quitando los borrados de las acciones. 
hmax calcula un plan para conseguir óptimamente cada una de las metas por separado, y con la que más coste le haya dado, determina el valor de la heurística. 

with OneshotPlanner(
    name="fast-downward",
    params={
        "search": "astar(hmax())"
    }
) as planner:
    result = planner.solve(problem)
'''

'''
Para generar planes subóptimos más rápido. 
OneshotPlanner(
    name="fast-downward",
    params={"search": "greedy([ff()])"}
)
'''

print(result.plan)