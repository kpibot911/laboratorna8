class Algorithms:
  # 1. Пошук мінімального елемента масиву позитивних чисел
  @staticmethod
  def find_min_positive(array):
      if not array or all(x <= 0 for x in array):
          raise ValueError("Масив повинен містити хоча б одне позитивне число.")
      return min(x for x in array if x > 0)

  # 2. Розрахунок суми від’ємних чисел масиву
  @staticmethod
  def sum_negative(array):
      return sum(x for x in array if x < 0)

  # 3. Розрахунок N-го елемента послідовності Фібоначчі
  @staticmethod
  def fibonacci(n):
      if n < 0:
          raise ValueError("N не може бути від’ємним.")
      if n == 0:
          return 0
      if n == 1:
          return 1
      a, b = 0, 1
      for _ in range(2, n + 1):
          a, b = b, a + b
      return b

  # 4. Розрахунок сили струму за законом Ома (I = U / R)
  @staticmethod
  def calculate_current(voltage, resistance):
      if resistance == 0:
          raise ValueError("Опір не може дорівнювати нулю.")
      return voltage / resistance
