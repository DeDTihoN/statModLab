import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, chi2
from collections import Counter


def simulate_poisson_distribution(lam, size=1000):
    # Генеруємо дані з розподілу Пуассона
    data = np.random.poisson(lam, size)

    # Оцінка експериментальних частот
    counts = Counter(data)
    total_count = sum(counts.values())

    # Обчислюємо середнє значення з експериментальних даних
    observed_mean = np.mean(data)

    # Виводимо вибране середнє значення та експериментальне середнє
    print(f"\nВибране середнє значення (λ): {lam}")
    print(f"Експериментальне середнє значення: {observed_mean:.3f}")
    print(f"Відхилення між очікуваним та експериментальним середнім: {abs(lam - observed_mean):.3f}")

    # Теоретичні частоти
    max_value = max(counts.keys())  # Максимальне значення випадкової величини для оцінки
    theoretical_probs = [poisson.pmf(k, lam) for k in range(max_value + 1)]
    expected_counts = [p * total_count for p in theoretical_probs]

    # Експериментальні частоти
    print("\nЕкспериментальні частоти:")
    for value, count in sorted(counts.items()):
        print(f"Значення {value}: частота {count / total_count:.3%}")

    # Хі-квадрат тест
    chi_square = sum((counts.get(k, 0) - expected_count) ** 2 / expected_count
                     for k, expected_count in enumerate(expected_counts) if expected_count > 0)
    degrees_of_freedom = len(expected_counts) - 1 - 1  # Кількість степенів свободи (значення - 1 - 1 параметр)
    critical_value = chi2.ppf(0.95, df=degrees_of_freedom)

    print(f"\nЗначення хі-квадрат: {chi_square:.3f}")
    print(f"Критичне значення хі-квадрат (95% рівень значущості): {critical_value:.3f}")

    if chi_square > critical_value:
        print("Результати не відповідають очікуваному розподілу (відхиляємо нульову гіпотезу).")
    else:
        print("Результати відповідають очікуваному розподілу (не відхиляємо нульову гіпотезу).")

    # Візуалізація
    plt.figure(figsize=(12, 6))

    # Експериментальні частоти
    values = list(range(max_value + 1))
    observed_frequencies = [counts.get(k, 0) / total_count for k in values]

    # Теоретичні частоти
    theoretical_frequencies = theoretical_probs

    # Побудова гістограми
    plt.bar(values, observed_frequencies, alpha=0.6, label='Експериментальні частоти', color='blue', edgecolor='black')
    plt.plot(values, theoretical_frequencies, marker='o', color='red', label='Теоретичні частоти', linestyle='dashed')
    plt.xlabel('Значення випадкової величини')
    plt.ylabel('Ймовірність')
    plt.title('Експериментальні та теоретичні частоти для розподілу Пуассона')
    plt.legend()
    plt.grid(True)
    plt.show()


# Введення параметрів
lam = float(input("Введіть значення параметру λ (середнє значення): "))
simulate_poisson_distribution(lam)
