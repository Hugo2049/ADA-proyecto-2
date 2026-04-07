# Coin Change Problem — Mínimo Número de Monedas
### Análisis y Diseño de Algoritmos — Sección 10
**Universidad del Valle de Guatemala**  
**Erick Guerra & Hugo Barillas**  
**Ing. Gabriel Brolo — 2026**

---

## 📹 Video de Presentación

[![Coin Change Problem](https://img.shields.io/badge/YouTube-Ver%20Video-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=3D5CQ3stz1U)

---

## 📌 Descripción del Problema

El *Coin Change Problem* consiste en encontrar el **mínimo número de monedas** cuya suma sea exactamente un monto objetivo `n`, dado un conjunto de denominaciones disponibles, asumiendo que se cuenta con una cantidad ilimitada de monedas de cada tipo.

Para este proyecto trabajamos con las denominaciones `C = {1, 5, 10, 25}` centavos, y desarrollamos dos algoritmos para resolver el problema: uno con la técnica **Divide and Conquer** y otro con **Programación Dinámica bottom-up**.

### Ejemplo

| Monto | Mín. monedas | Combinación óptima |
|-------|-------------|-------------------|
| 11    | 2           | 10 + 1            |
| 15    | 2           | 10 + 5            |
| 25    | 1           | 25                |
| 30    | 2           | 25 + 5            |

---

## 📁 Estructura del Repositorio

```
ADA-proyecto-2/
├── coin_change_dac.py     # Algoritmo Divide and Conquer
├── coin_change_dp.py      # Algoritmo Programación Dinámica
├── tiempos_dac.csv        # Resultados empíricos DaC
├── tiempos_dp.csv         # Resultados empíricos DP
├── proyecto2.tex          # Documento LaTeX con análisis completo
├── proyecto2.pdf          # Documento PDF compilado
└── README.md
```

---

## ⚙️ Cómo ejecutar los algoritmos

Se necesita tener **Python 3** instalado, no se requieren librerías externas.

```bash
# Algoritmo Divide and Conquer
python coin_change_dac.py

# Algoritmo Programación Dinámica
python coin_change_dp.py
```

Cada script imprime en consola una tabla con el monto, el número mínimo de monedas y el tiempo de ejecución, y genera un archivo `.csv` con los resultados listos para graficar.

---

## 🔀 Algoritmo 1 — Divide and Conquer

El enfoque DaC resuelve el problema de forma **recursiva pura**, sin reutilizar resultados previos. Para cada llamada con monto `n`, divide el problema en `k` subproblemas (uno por cada denominación), resuelve cada uno recursivamente y combina los resultados tomando el mínimo.

```python
def coin_change_dac(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return inf

    min_coins = inf
    for coin in coins:                           # Divide
        result = coin_change_dac(coins,
                                 amount - coin)  # Conquer
        if result != inf:
            min_coins = min(min_coins,
                            result + 1)          # Combine
    return min_coins
```

**Complejidad teórica:** la recurrencia es `T(n) = 4·T(n-1) + Θ(1)`, que resuelta por sustitución da **Θ(4ⁿ)** — exponencial en el monto objetivo.

---

## 📋 Algoritmo 2 — Programación Dinámica (Bottom-Up)

El enfoque DP construye una tabla `dp[0..n]` donde `dp[m]` almacena el mínimo de monedas para el monto `m`, resolviendo primero los subproblemas más pequeños y reutilizando sus soluciones para los más grandes, de forma análoga al *Rod-Cutting Problem* visto en clase.

```python
def coin_change_dp(coins, amount):
    dp = [inf] * (amount + 1)
    dp[0] = 0                          # caso base

    for m in range(1, amount + 1):     # bottom-up
        for coin in coins:
            if coin <= m and dp[m - coin] != inf:
                dp[m] = min(dp[m],
                            dp[m - coin] + 1)

    return dp[amount] if dp[amount] != inf else -1
```

**Complejidad teórica:** dos ciclos anidados de `n` y `k` iteraciones respectivamente, con operaciones internas de costo constante, dan una complejidad de **Θ(n)** con `k` fijo.

---

## 📊 Análisis Empírico

Ejecutamos ambos algoritmos sobre las mismas **30 entradas** (montos del 1 al 30), midiendo el tiempo con `time.perf_counter()` de Python.

### Resultados destacados

| Monto | DaC (s)     | DP (s)      | DaC / DP |
|-------|-------------|-------------|----------|
| 10    | 0.0000300   | 0.0000143   | ~2x      |
| 20    | 0.0003059   | 0.0000204   | ~15x     |
| 25    | 0.0015783   | 0.0000209   | ~75x     |
| 30    | 0.0078119   | 0.0000165   | **~473x**|

### Observaciones

**DaC:** los tiempos crecen de forma claramente exponencial, pasando de microsegundos en montos pequeños a milisegundos en montos cercanos a 30, confirmando el comportamiento Θ(4ⁿ) predicho teóricamente, con ruido propio de mediciones en el orden de los microsegundos para entradas pequeñas.

**DP:** los tiempos se mantienen prácticamente estables en todo el rango probado, todos en el orden de los microsegundos, consistente con la complejidad Θ(n), cuya tendencia lineal se apreciaría de forma más clara con montos en el orden de los miles.

**Comparación:** para el monto 30, el DaC fue aproximadamente **473 veces más lento** que la DP, una diferencia que crece exponencialmente con el monto, haciendo al DaC completamente impracticable para valores mayores a 40 o 50 con las denominaciones elegidas.

---

## 📄 Documento de Análisis

El archivo `proyecto2.pdf` contiene el análisis completo del proyecto, incluyendo la definición formal del problema, los pseudocódigos con su justificación teórica, el desarrollo matemático de las recurrencias, las gráficas comparativas y los comentarios sobre los resultados empíricos.

---

## 👥 Autores

- **Erick Guerra**
- **Hugo Barillas**
