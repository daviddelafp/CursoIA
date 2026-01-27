(define (domain blocksworld) ;definir el dominio del mundo de bloques
  (:requirements :strips :typing) ;requerimientos del dominio STRIPS(AND NOT) y typing
  (:types block) ;definir el tipo bloque

  (:predicates ;predicados son los hechos posibles del mundo
    (on ?x - block ?y - block)  ;El bloque x esta sobre el bloque y
    (ontable ?x - block)  ; ;El bloque x esta sobre la mesa
    (clear ?x - block) ; El bloque x no tiene ningun bloque encima
    (holding ?x - block) ; El robot sostiene el bloque x
    (handempty) ; La mano del robot esta vacia
  )

  (:action pickup ;accion de recoger un bloque
    :parameters (?x - block) ; parametro x de tipo bloque
    :precondition (and (ontable ?x) (clear ?x) (handempty)) ;precondiciones para recoger el bloque x
    :effect (and ; efectos de la accion pickup
      (not (ontable ?x)) ; el bloque x ya no esta sobre la mesa
      (not (clear ?x)) ; el bloque x ya no esta libre
      (not (handempty)) ; la mano del robot ya no esta vacia
      (holding ?x)) ; el robot sostiene el bloque x
  )

  (:action putdown ;accion de dejar un bloque
    :parameters (?x - block) ; parametro x de tipo bloque
    :precondition (holding ?x) ;precondicion para dejar el bloque x Que lo sujete
    :effect (and ; efectos de la accion putdown
      (ontable ?x) ; el bloque x esta sobre la mesa
      (clear ?x) ; el bloque x esta libre
      (handempty) ; la mano del robot esta vacia
      (not (holding ?x))) ; el robot ya no sostiene el bloque x
  )

  (:action stack ; accion de apilar un bloque sobre otro
    :parameters (?x - block ?y - block) ; parametros x e y de tipo bloque
    :precondition (and (holding ?x) (clear ?y)) ; precondiciones para apilar el bloque x sobre el bloque y
    :effect (and ; efectos de la accion stack
      (on ?x ?y) ; el bloque x esta sobre el bloque y
      (clear ?x) ; el bloque x esta libre
      (handempty) ; la mano del robot esta vacia
      (not (holding ?x)) ; el robot ya no sostiene el bloque x
      (not (clear ?y))) ; el bloque y ya no esta libre
  )

  (:action unstack ; accion de desapilar un bloque de otro
    :parameters (?x - block ?y - block) ; parametros x e y de tipo bloque
    :precondition (and (on ?x ?y) (clear ?x) (handempty)) ; precondiciones para desapilar el bloque x del bloque y
    :effect (and ; efectos de la accion unstack
      (holding ?x) ; el robot sostiene el bloque x
      (clear ?y) ; el bloque y esta libre
      (not (on ?x ?y)) ; el bloque x ya no esta sobre el bloque y
      (not (clear ?x)) ; el bloque x ya no esta libre
      (not (handempty))) ; la mano del robot ya no esta vacia
  )
)
