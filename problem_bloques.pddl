(define (problem bw-3) ; definir el problema bw-3
  (:domain blocksworld) ; especificar el dominio blocksworld

  (:objects a b c - block) ; definir los objetos a, b y c como bloques

  (:init ; estado inicial del problema
    (ontable a) ; el bloque a esta sobre la mesa
    (ontable b) ; el bloque b esta sobre la mesa
    (ontable c) ; el bloque c esta sobre la mesa
    (clear a) ; el bloque a esta libre
    (clear b) ; el bloque b esta libre
    (clear c) ; el bloque c esta libre
    (handempty) ; la mano del robot esta vacia
  )

  (:goal ; objetivo del problema
    (and ; los bloques deben estar apilados en el siguiente orden
      (on a b) ; el bloque a esta sobre el bloque b
      (on b c) ; el bloque b esta sobre el bloque c
    )
  )
)
