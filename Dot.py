
class Dot:

    SIGNS = {
        "my_ship": "\U0001F7E6", "enemy_ship": "\U0001F7E5", "empty_dot": "⬜",
        "destroy": "❌", "miss": "✖️ ", "three_health": "🩸", "two_health": "📛",
        "one_health": "🔥"
    }

    def __init__(self, x, y, sigh) -> None:
        self.x = x
        self.y = y
        self.sigh = self.SIGNS.get(sigh)

    def change_dot(self, sigh) -> None:
        self.sigh = self.SIGNS.get(sigh)

    def __str__(self) -> str:
        return f"{self.sigh}"
