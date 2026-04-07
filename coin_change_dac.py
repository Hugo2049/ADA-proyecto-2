import time
import math


def coin_change_dac(coins, amount):
    """
    Coin Change Problem - Divide and Conquer (recursion pura, sin memoizacion).
    Divide el problema en subproblemas mas pequenos restando una moneda a la vez
    y combina resultados tomando el minimo
    """
    # Caso base
    if amount == 0:
        return 0
    if amount < 0:
        return math.inf

    min_coins = math.inf

    # Divide: prueba cada moneda y reduce el problema
    for coin in coins:
        result = coin_change_dac(coins, amount - coin)
        # Conquer: toma el mejor resultado
        if result != math.inf:
            min_coins = min(min_coins, result + 1)

    return min_coins


# ──────────────────────────────────────────────
# Medicion de tiempos
# ──────────────────────────────────────────────
if __name__ == "__main__":
    coins = [1, 5, 10, 25]  # denominaciones en centavos

    # 30 entradas de prueba (montos del 1 al 30)
    # NOTA: DaC puro es exponencial; montos > 30 pueden tardar mucho.
    test_inputs = list(range(1, 31))

    print(f"{'Monto':>8} | {'Monedas':>8} | {'Tiempo (s)':>14}")
    print("-" * 38)

    results = []

    for amount in test_inputs:
        start = time.perf_counter()
        answer = coin_change_dac(coins, amount)
        end = time.perf_counter()

        elapsed = end - start
        results.append((amount, answer, elapsed))

        ans_str = str(answer) if answer != math.inf else "imposible"
        print(f"{amount:>8} | {ans_str:>8} | {elapsed:>14.8f}")

    # Guardar CSV para graficar despues
    with open("tiempos_dac.csv", "w") as f:
        f.write("monto,monedas,tiempo_s\n")
        for amount, answer, elapsed in results:
            ans_str = str(answer) if answer != math.inf else "-1"
            f.write(f"{amount},{ans_str},{elapsed}\n")

    print("\nResultados guardados en tiempos_dac.csv")