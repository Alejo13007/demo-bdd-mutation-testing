# language: es
Característica: Retiro de dinero en Cajero Automatico

  Escenario: Retiro exitoso cuando hay saldo suficiente
    Dado que el cliente tiene un saldo disponible de 1000 pesos
    Cuando solicita retirar 300 pesos
    Entonces la operacion es "RETIRO_EXITOSO"
    Y el nuevo saldo disponible es de 700 pesos

  Escenario: Rechazo de retiro por saldo insuficiente
    Dado que el cliente tiene un saldo disponible de 500 pesos
    Cuando solicita retirar 600 pesos
    Entonces la operacion es "SALDO_INSUFFICIENTE"
    Y el nuevo saldo disponible es de 500 pesos

  @limite
  Escenario: Retiro por el monto exacto del saldo disponible
    Dado que el cliente tiene un saldo disponible de 500 pesos
    Cuando solicita retirar 500 pesos
    Entonces la operacion es "RETIRO_EXITOSO"
    Y el nuevo saldo disponible es de 0 pesos
