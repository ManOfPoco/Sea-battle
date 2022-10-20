class Dot:

    SIGNS = {
        "my_ship": "🟦", "secondplayer_ship": "🟥", "hit": "❌",
        "miss": "✖️", "empty_dot": "⬜"
    }

    def __init__(self, x, y, sigh) -> None:
        self.x = x
        self.y = y
        self.sigh = self.SIGNS.get(sigh)

    def change_dot(self, sigh) -> None:
        self.sigh = self.SIGNS.get(sigh)

    def __str__(self) -> str:
        return f"{self.sigh}"
