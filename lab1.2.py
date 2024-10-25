import random
from collections import Counter

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
    for num in range(1, 7):
        observed_probability = total_counts[num] / total_rolls  # Отримана ймовірність
        difference = observed_probability - expected_probability  # Відхилення від очікуваної ймовірності
        print(f"Цифра {num}: випадінь {total_counts[num]}, ймовірність {observed_probability:.3%}, відхилення {difference:.2%}")

# Введіть кількість підкидань N
N = int(input("Введіть кількість підкидань (N): "))

simulate_dice_rolls(N)
