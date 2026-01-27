(define (problem nombre) ; definir el problema nombre
  (:domain blocksworld) ; especificar el dominio blocksworld

  (:objects d a v i d2 - block) ; definir los objetos a, b y c como bloques

  (:init ; estado inicial del problema
    (ontable d) ; el bloque d esta sobre la mesa
    (ontable a) ; el bloque a esta sobre la mesa
    (ontable v) ; el bloque v esta sobre la mesa
    (ontable i) ; el bloque i esta sobre la mesa
    (ontable d2) ; el bloque d2 esta sobre la mesa
    (clear d) ; el bloque d esta libre
    (clear a) ; el bloque a esta libre
    (clear v) ; el bloque v esta libre
    (clear i) ; el bloque i esta libre
    (clear d2) ; el bloque d2 esta libre
    (handempty) ; la mano del robot esta vacia
  )

  (:goal ; objetivo del problema
    (and ; los bloques deben estar apilados en el siguiente orden
      (ontable d) ; el bloque d esta sobre la mesa
      (on a d) ; el bloque a esta sobre el bloque d
      (on v a) ; el bloque v esta sobre el bloque a
      (on i v) ; el bloque i esta sobre el bloque v
      (on d2 i) ; el bloque d2 esta sobre el bloque i
    )
  )
)
