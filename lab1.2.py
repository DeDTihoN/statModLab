import random
from collections import Counter
import matplotlib.pyplot as plt
from scipy.stats import chi2  # Для обчислення критичного значення хі-квадрат

def simulate_dice_rolls(N, K=11):
    # Ініціалізуємо лічильник для підсумкової кількості випадінь кожної цифри за всі симуляції
    total_counts = Counter({i: 0 for i in range(1, 7)})
    total_rolls = N * K  # Загальна кількість підкидань за всі симуляції
    expected_probability = 1 / 6  # Очікувана ймовірність для кожної цифри

    for simulation in range(K):
        # Лічильник для кожної окремої симуляції
        single_simulation_counts = Counter(random.randint(1, 6) for _ in range(N))

        # Додаємо результат окремої симуляції до загальної кількості
        for num in range(1, 7):
            total_counts[num] += single_simulation_counts.get(num, 0)

        print(f"Результати {simulation + 1}-ї симуляції: {single_simulation_counts}")

    # Виводимо загальну кількість випадінь для кожної цифри за всі симуляції
    print("\nЗагальна кількість випадінь для кожної цифри за всі симуляції:")
    observed_probabilities = []
    expected_count = total_rolls / 6  # Очікувана кількість випадінь для кожної цифри
    chi_square = 0  # Ініціалізуємо значення хі-квадрат

    for num in range(1, 7):
        observed_probability = total_counts[num] / total_rolls  # Отримана ймовірність
        difference = observed_probability - expected_probability  # Відхилення від очікуваної ймовірності
        observed_probabilities.append(observed_probability * 100)  # Відсотки для графіка

        # Обчислюємо хі-квадрат для поточної цифри
        chi_square += (total_counts[num] - expected_count) ** 2 / expected_count

        print(f"Цифра {num}: випадінь {total_counts[num]}, ймовірність {observed_probability:.3%}, відхилення {difference:.2%}")

    # Хі-квадрат тест
    critical_value = chi2.ppf(0.95, df=5)  # 95% рівень значущості, 5 ступенів свободи (6-1)
    print(f"\nЗначення хі-квадрат: {chi_square:.3f}")
    print(f"Критичне значення хі-квадрат (95% рівень значущості): {critical_value:.3f}")

    if chi_square > critical_value:
        print("Результати не відповідають очікуваному розподілу (відхиляємо нульову гіпотезу).")
    else:
        print("Результати відповідають очікуваному розподілу (не відхиляємо нульову гіпотезу).")

    # Побудова графіку
    numbers = list(range(1, 7))
    counts = [total_counts[num] for num in numbers]

    plt.figure(figsize=(12, 6))

    # Графік кількості випадінь
    plt.subplot(1, 2, 1)
    plt.bar(numbers, counts, color='lightblue', edgecolor='black', label='Фактичні випадіння')
    plt.axhline(y=expected_count, color='red', linestyle='--', label='Очікувана кількість')
    plt.xlabel('Цифри на кубику')
    plt.ylabel('Кількість випадінь')
    plt.title('Кількість випадінь для кожної цифри')
    plt.legend()

    # Графік ймовірностей
    plt.subplot(1, 2, 2)
    plt.bar(numbers, observed_probabilities, color='lightgreen', edgecolor='black', label='Фактична ймовірність')
    plt.axhline(y=expected_probability * 100, color='red', linestyle='--', label='Очікувана ймовірність (16.67%)')
    plt.xlabel('Цифри на кубику')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності випадіння кожної цифри')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Введіть кількість підкидань N
N = int(input("Введіть кількість підкидань (N): "))

simulate_dice_rolls(N)
