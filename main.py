from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Colour as DiscordColor
from RandomColorRoleClient import RandomColorRoleClient
from random_color_strategies import RandomColor, light_mode_friendly_strategy, dark_mode_dominant_strategy
from color_utils import to_color
# import plotext as plt
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    load_dotenv()
    TOKEN: Final[str | None] = os.getenv('DISCORD_TOKEN')

    if not TOKEN:
        print('missing token')
        return

    client: Client = RandomColorRoleClient(intents=Intents.default())
    client.run(token=TOKEN)


def test() -> None:
    dark_theme_color = to_color(DiscordColor.dark_theme())
    print(f'Dark theme color: {dark_theme_color.to_string(hex=True)}')
    light_mode_random_color = RandomColor(light_mode_friendly_strategy)
    dark_mode_random_color = RandomColor(dark_mode_dominant_strategy)
    # test_colors1 = [strict_random_color.generate() for _ in range(5000)]
    # ratios1 = [color.contrast(dark_theme_color) for color in test_colors1]
    # plt.hist(ratios1, norm=True)
    # plt.show()
    # plt.clear_data()
    # print(len([True for ratio in ratios1 if ratio < 2.5]))
    # test_colors2 = [lenient_random_color.generate() for _ in range(5000)]
    # ratios2 = [color.contrast(dark_theme_color) for color in test_colors2]
    # plt.hist(ratios2, norm=True)
    # plt.show()
    # print(
    #     len([
    #         True
    #         for color
    #         in test_colors2
    #         if color.contrast(Color('white')) < 2.0])/5000)
    colors3 = [dark_mode_random_color.generate() for _ in range(200)]
    colors3.sort(key=lambda c: c.convert('oklch')['c'])
    # colors3.sort(key=lambda c: c.contrast(dark_theme_color))
    color_strings = [
        (colored(
            int(color['r']*255),
            int(color['g']*255),
            int(color['b']*255),
            '████'))
        for color in colors3]
    # print(*color_strings, sep='')

    colors4 = [dark_mode_random_color.generate() for _ in range(1000)]
    colors4oklch = np.array([c.convert('oklch').coords()
                            for c in colors4]).transpose()
    colors4pltcolors = np.array([c[:-1] for c in colors4])
    colors4.sort(key=lambda c: c.convert('oklch')['l'])
    fig, ax = plt.subplots(ncols=1, nrows=2)
    ax[0].scatter(colors4oklch[2], colors4oklch[1], c=colors4pltcolors)
    ax[0].set_ylabel('Chroma')
    ax[1].scatter(colors4oklch[2], colors4oklch[0], c=colors4pltcolors)
    ax[1].set_xlabel('Hue')
    ax[1].set_ylabel('Lightness')
    fig.show()


# https://stackoverflow.com/a/61960902/2438757
def colored(r: int, g: int, b: int, text: str) -> str:
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


if __name__ == '__main__':
    main()
