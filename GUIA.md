# Demo de BDD & Mutation Testing (Sistema de Retiro Bancario)

Este proyecto es una demostración aislada del funcionamiento de **Behavior-Driven Development (BDD)** usando `pytest-bdd` y **Mutation Testing** con `mutmut`.

---

## 📋 Requisitos Previos

1. **Python 3.10+**
2. **Entorno Unix/Linux** (WSL en Windows o una Máquina Virtual con Linux).
   > **Nota importante:** `mutmut` requiere la llamada al sistema `fork()`, la cual no existe de forma nativa en PowerShell o CMD de Windows. Por ello, la ejecución debe hacerse dentro de WSL o Linux.

---

## 🛠️ Configuración del Entorno (WSL / Linux)

### 1. Preparar la terminal
Abre la carpeta `demo_presentacion` en VS Code, inicia una terminal integrada (`Ctrl + ~`) e ingresa a WSL ejecutando:

```bash
wsl
```

### 2. Instalar dependencias del sistema (Debian/Ubuntu)
Si estás iniciando en WSL por primera vez, instala el paquete de entornos virtuales de Python:

```bash
sudo apt update
sudo apt install -y python3-venv
```

### 3. Crear y activar el entorno virtual

```bash
python3 -m venv .venv_wsl
source .venv_wsl/bin/activate
```

*(Una vez activado, verás `(.venv_wsl)` al comienzo de la línea de comandos).*

### 4. Instalar paquetes de Python

```bash
pip install pytest pytest-bdd mutmut
```

---

## 📁 Estructura del Proyecto

```text
demo_presentacion/
│
├── src/
│   └── cuenta.py            # Lógica de negocio (CuentaBancaria)
│
├── features/
│   └── retiro.feature       # Escenarios BDD descritos en lenguaje Gherkin
│
├── tests/
│   └── test_retiro.py       # Definición e implementación de pasos BDD (pytest-bdd)
│
├── pyproject.toml           # Configuración de pytest y mutmut
└── README.md                # Este documento
```

---

## 🚀 1. Ejecución de Pruebas BDD (`pytest-bdd`)

Para verificar que todos los escenarios descritos en Gherkin se ejecutan correctamente:

```bash
pytest -v
```

Deberías ver que los escenarios pasan en verde (**PASSED**).

---

## 🧪 2. Ejecución de Mutation Testing (`mutmut`)

Mutation Testing introduce pequeñas modificaciones deliberadas (mutantes) en el código fuente (`src/cuenta.py`) para evaluar si la suite de pruebas es capaz de detectar fallas.

### A. Correr el análisis de mutaciones

```bash
mutmut run
```

### B. Ver los resultados (Killed vs Survived)

```bash
mutmut results
```

Salida esperada: Muestra los mutantes eliminados (🎉) y aquellos que sobrevivieron (😟), junto con el identificador asignado a cada uno.

### C. Inspeccionar el cambio introducido por un mutante

```bash
mutmut show 'cuenta.xǁCuentaBancariaǁretirar__mutmut_1'
```


### D. Reiniciar la caché si es necesario

```bash
rm -f .mutmut-cache
mutmut run
```

---

