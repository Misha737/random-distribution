# Random distribution
Програма призначення для відображення розподілу ймовірності дискретним випадковим величинам у стовпчастій діаграмі

Ввід даних відбувається за допомогою аргументів командного рядка.
На вхід приймається список із випадкових величин та список із їх кількості.
Можна ввести список із ймовірності, програма це відобразить

Синтаксис можна подивитись в:
```
py main.py -h
```

Програма повинна відобразити стовпчасту діаграму, де значенням є ймовірність випадкової величини
Також програма відображає пряму математичного сподівання (Expected value) та значення дисперсії (Variance)

## Структура програми
1. Обробка вводу даних користувача
2. Клас Distribution, відповідає за механіку випадкового розподілу (Random distribution)
   * Знаходження математичного сподівання
   * Знаходження значення дисперсії
   * Та інше
3. Створення стовпчастої діаграми

## Additional task
1. Відображення значення стовпця діаграми при наведенні миші
2. Якщо на вхід було введено список із ймовірності випадкової величини, це відобразиться на графіку.
Це було зроблено за для того, щоб при веденні користувачем список із ймовірностей, користувач впевнився, що значення були
введені правильно і діаграма побудувалась коректно

> **P.S.** Автор цього проєкту був натхненний базовою теорією ймовірностей 