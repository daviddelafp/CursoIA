from unified_planning.io import PDDLReader
from unified_planning.shortcuts import OneshotPlanner

reader = PDDLReader()
problem = reader.parse_problem("domain_patinador.pddl", "problemaPatinador.pddl")

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

print(result.plan)

'''
Secuential plan: 
pickup(b)  ; recoger el bloque b
stack(b, c) ; apilar el bloque b sobre el bloque c
pickup(a) ; recoger el bloque a
stack(a, b) ; apilar el bloque a sobre el bloque b
'''