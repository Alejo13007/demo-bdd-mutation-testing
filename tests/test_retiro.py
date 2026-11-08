import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from cuenta import CuentaBancaria

# -------------------------------------------------------------
# 1. VINCULACIÓN BDD (pytest-bdd)
# -------------------------------------------------------------
scenarios("features/retiro.feature")

@given(parsers.parse("que el cliente tiene un saldo disponible de {saldo:d} pesos"), target_fixture="cuenta")
def inicializar_cuenta(saldo):
    return CuentaBancaria(saldo_inicial=float(saldo))

@when(parsers.parse("solicita retirar {monto:d} pesos"), target_fixture="resultado")
def realizar_retiro(cuenta, monto):
    return cuenta.retirar(monto=float(monto))

@then(parsers.parse('la operacion es "{esperado}"'))
def verificar_resultado(resultado, esperado):
    assert resultado == esperado

@then(parsers.parse("el nuevo saldo disponible es de {saldo_esperado:d} pesos"))
def verificar_saldo(cuenta, saldo_esperado):
    assert cuenta.saldo == float(saldo_esperado)