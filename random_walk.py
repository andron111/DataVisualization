from random import choice


class RandomWalk():
    """Класс для генерирования случайных блужданиий."""

    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждения."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]
