import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rayleigh, chi2
from collections import Counter


def simulate_rayleigh_distribution(sigma, size=1000):
    # Генерація незалежних нормальних випадкових величин η1 і η2
    eta1 = np.random.normal(0, sigma, size)
    eta2 = np.random.normal(0, sigma, size)

    # Моделюємо випадкову величину з розподілом Релея
    rayleigh_data = np.sqrt(eta1 ** 2 + eta2 ** 2)

    # Оцінка експериментальних частот
    counts, bin_edges = np.histogram(rayleigh_data, bins=20, range=(0, rayleigh_data.max()), density=False)
    total_count = np.sum(counts)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # Теоретичні частоти для Релеєвського розподілу
    theoretical_probs = rayleigh.pdf(bin_centers, scale=sigma)
    expected_counts = theoretical_probs * total_count * (bin_edges[1] - bin_edges[0])

    # Хі-квадрат тест
    chi_square = np.sum((counts - expected_counts) ** 2 / expected_counts)
    degrees_of_freedom = len(counts) - 1 - 1  # Кількість степенів свободи (кількість інтервалів - 1 - 1 параметр)
    critical_value = chi2.ppf(0.95, df=degrees_of_freedom)

    print(f"\nЗначення хі-квадрат: {chi_square:.3f}")
    print(f"Критичне значення хі-квадрат (95% рівень значущості): {critical_value:.3f}")

    if chi_square > critical_value:
        print("Результати не відповідають очікуваному розподілу Релея (відхиляємо нульову гіпотезу).")
    else:
        print("Результати відповідають розподілу Релея (не відхиляємо нульову гіпотезу).")

    # Візуалізація
    plt.figure(figsize=(12, 6))

    # Експериментальна гістограма
    plt.hist(rayleigh_data, bins=20, density=True, alpha=0.6, color='skyblue', edgecolor='black',
             label='Експериментальні дані')

    # Теоретична щільність Релея
    x = np.linspace(0, rayleigh_data.max(), 1000)
    plt.plot(x, rayleigh.pdf(x, scale=sigma), 'r--', label='Теоретична щільність Релея')

    plt.xlabel('Значення випадкової величини')
    plt.ylabel('Ймовірність')
    plt.title('Експериментальна та теоретична щільності для розподілу Релея')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Розрахунок дисперсії
    observed_variance = np.var(rayleigh_data)
    theoretical_variance = sigma ** 2 * (2 - np.pi / 2)
    variance_difference = abs(observed_variance - theoretical_variance)

    print(f"\nТеоретична дисперсія: {theoretical_variance:.3f}")
    print(f"Експериментальна дисперсія: {observed_variance:.3f}")
    print(f"Відхилення між теоретичною та експериментальною дисперсією: {variance_difference:.3f}")


# Введення параметра σ
sigma = float(input("Введіть значення параметру σ: "))
simulate_rayleigh_distribution(sigma)
