import random
import matplotlib.pyplot as plt
from scipy.stats import chi2  # Для обчислення критичного значення хі-квадрат

def simulate_coin_tosses(N, K):
    total_heads = 0  # Загальна кількість випадінь "герба" за всі підходи
    total_tails = 0  # Загальна кількість випадінь "решки" за всі підходи

    for _ in range(K):
        heads_in_single_simulation = sum(1 for _ in range(N) if random.choice(['heads', 'tails']) == 'heads')
        tails_in_single_simulation = N - heads_in_single_simulation

        print(f"В окремій симуляції випало гербів: {heads_in_single_simulation}")
        total_heads += heads_in_single_simulation
        total_tails += tails_in_single_simulation

    print(f"\nЗагальна кількість випадінь герба за всі симуляції: {total_heads}")
    print(f"Загальна кількість випадінь решки за всі симуляції: {total_tails}")

    GENERAL_PROBABILITY = 0.5
    GENERAL_TOSSES = N * K
    PROBABILITY_DIFFERENCE = abs(GENERAL_PROBABILITY - (total_heads / GENERAL_TOSSES))
    print(f"\nРізниця між теоритичною та практичною ймовірністю: {PROBABILITY_DIFFERENCE}")

    # Хі-квадрат тест
    expected_count = GENERAL_TOSSES / 2
    chi_square = ((total_heads - expected_count) ** 2 / expected_count) + \
                 ((total_tails - expected_count) ** 2 / expected_count)
    critical_value = chi2.ppf(0.95, df=1)  # 95% рівень значущості, 1 ступінь свободи
    print(f"\nЗначення хі-квадрат: {chi_square:.3f}")
    print(f"Критичне значення хі-квадрат (95% рівень значущості): {critical_value:.3f}")

    if chi_square > critical_value:
        print("Результати не відповідають очікуваному розподілу (відхиляємо нульову гіпотезу).")
    else:
        print("Результати відповідають очікуваному розподілу (не відхиляємо нульову гіпотезу).")

    # Побудова графіку
    labels = ['Heads', 'Tails']
    percentages = [total_heads / GENERAL_TOSSES * 100, total_tails / GENERAL_TOSSES * 100]

    plt.bar(labels, percentages, color=['blue', 'orange'])
    plt.title('Відсоток випадінь кожної сторони монети')
    plt.ylabel('Відсоток (%)')
    plt.ylim(0, 100)
    plt.show()

# Введіть значення N та K
N = int(input("Введіть кількість підкидань (N): "))
K = int(input("Введіть кількість симуляцій (K): "))

simulate_coin_tosses(N, K)
