import time
import math


def coin_change_dp(coins, amount):
    """
    Coin Change Problem - Programacion Dinamica Bottom-Up.
    Construye la solucion optima desde los subproblemas mas pequenos
    hasta el monto objetivo (igual al enfoque del Rod-Cutting Problem visto en clase).

    Args:
        coins  : lista de denominaciones disponibles
        amount : monto objetivo

    Returns:
        Minimo numero de monedas, o -1 si no es posible.
    """
    # Tabla dp: dp[m] = minimo de monedas para el monto m
    dp = [math.inf] * (amount + 1)
    dp[0] = 0  # caso base: 0 monedas para monto 0

    # Bottom-up: resuelve cada submonto de 1 hasta amount
    for m in range(1, amount + 1):
        for coin in coins:
            if coin <= m and dp[m - coin] != math.inf:
                dp[m] = min(dp[m], dp[m - coin] + 1)

    return dp[amount] if dp[amount] != math.inf else -1


# ──────────────────────────────────────────────
# Medicion de tiempos
# ──────────────────────────────────────────────
if __name__ == "__main__":
    coins = [1, 5, 10, 25]  # denominaciones en centavos

    # 30 entradas de prueba — mismas que en DaC para comparar
    test_inputs = list(range(1, 31))

    print(f"{'Monto':>8} | {'Monedas':>8} | {'Tiempo (s)':>14}")
    print("-" * 38)

    results = []

    for amount in test_inputs:
        start = time.perf_counter()
        answer = coin_change_dp(coins, amount)
        end = time.perf_counter()

        elapsed = end - start
        results.append((amount, answer, elapsed))

        ans_str = str(answer) if answer != -1 else "imposible"
        print(f"{amount:>8} | {ans_str:>8} | {elapsed:>14.8f}")

    # Guardar CSV para graficar despues
    with open("tiempos_dp.csv", "w") as f:
        f.write("monto,monedas,tiempo_s\n")
        for amount, answer, elapsed in results:
            f.write(f"{amount},{answer},{elapsed}\n")

    print("\nResultados guardados en tiempos_dp.csv")