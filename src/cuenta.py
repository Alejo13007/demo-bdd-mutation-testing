class CuentaBancaria:
    def __init__(self, saldo_inicial: float):
        self.saldo = saldo_inicial

    def retirar(self, monto: float) -> str:
        if monto <= 0:
            return "MONTO_INVALIDO"
        # Regla de negocio: Si el monto supera el saldo disponible, rechaza
        if monto > self.saldo:
            return "SALDO_INSUFFICIENTE"
        
        self.saldo -= monto
        return "RETIRO_EXITOSO"