import random


def simulate_coin_tosses(N, K):
    total_heads = 0  # Загальна кількість випадінь "герба" за всі підходи

    for _ in range(K):
        heads_in_single_simulation = sum(1 for _ in range(N) if random.choice(['heads', 'tails']) == 'heads')
        print(f"В окремій симуляції випало гербів: {heads_in_single_simulation}")
        total_heads += heads_in_single_simulation

    print(f"\nЗагальна кількість випадінь герба за всі симуляції: {total_heads}")

    GENERAL_PROBABILITY = 0.5

    GENERAL_TOSSES = N * K

    PROBABILITY_DIFFERENCE = abs(GENERAL_PROBABILITY - (total_heads / GENERAL_TOSSES))

    print(f"\nРізниця між теоритичною та практичною ймовірностю: {PROBABILITY_DIFFERENCE}")

# Введіть значення N та K
N = int(input("Введіть кількість підкидань (N): "))
K = int(input("Введіть кількість симуляцій (K): "))

simulate_coin_tosses(N, K)
