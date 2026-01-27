(define (domain patinador-ice) ;definición del dominio
  (:requirements :strips :typing) ; requisitos del dominio
  (:types posicion) ; definición de tipos

  (:predicates
    (at_robot ?pos1 - posicion) ; el patinador está en la posición ?c
    (passable ?c - posicion) ; la posición ?c es transitable
   )

  (:action move ; definición de la acción de movimiento
    :parameters (?from - cell ?d - dir ?to - cell) ; que esté en una celda y se deslice en una dirección hacia otra celda
    :precondition (and (at ?from) (slide ?from ?d ?to) (passable ?to) (ice ?to) ) ; que esté en la celda ?from y pueda deslizarse hacia ?to
    :effect (and (not (at ?from)) (at ?to)) ; efecto: ya no está en ?from y ahora está en ?to
  )
)

