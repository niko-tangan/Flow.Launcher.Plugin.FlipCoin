import sys
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

from flowlauncher import FlowLauncher
import webbrowser


class CoinFlip(FlowLauncher):
    def query(self, query):
        return [
            {
                "title": f"You flipped a coin and got: {self.flip_coin()}!",
                "subTitle": "This is where your subtitle goes, press enter to open Flow's url",
                "icoPath": "Images/app.png",
                "score": 0,
            }
        ]

    def flip_coin(self):
        from random import randint

        return "Tails" if randint(0, 100) % 2 else "Heads"


if __name__ == "__main__":
    CoinFlip()
