from coloraide import Color
from discord import Colour as DiscordColor
from collections.abc import Callable, Sequence
from color_utils import to_color

_DISCORD_DARK_THEME = to_color(DiscordColor.dark_theme())
_WHITE = Color('#ffffff')


class RandomColor:
    def __init__(self, strategy: Callable[[], Color]) -> None:
        self.strategy = strategy

    def generate(self) -> Color:
        return self.strategy()


def light_mode_friendly_strategy() -> Color:
    color_contrast_pairs = [
        (_DISCORD_DARK_THEME, 2.5),
        (_WHITE, 2.0),
    ]
    return _contrast_based_strategy(color_contrast_pairs)


def dark_mode_dominant_strategy() -> Color:
    color_contrast_pairs = [
        (_DISCORD_DARK_THEME, 2.5),
        (_WHITE, 1.2),
    ]
    limits = [None, [0.11, 0.34], None]
    return _contrast_based_strategy(color_contrast_pairs, limits=limits)


def _contrast_based_strategy(
    color_contrast_pairs: Sequence[tuple[Color, float]],
    space: str = 'oklch',
    limits: Sequence[Sequence[float] | None] | None = None
) -> Color:
    while True:
        color = Color.random(space, limits=limits)
        if (color.in_gamut('srgb') and
                _is_contrast_compatible(color, color_contrast_pairs)):
            return color.convert('srgb').fit('srgb')


def _is_contrast_compatible(text_color: Color,
                            color_contrast_pairs: Sequence[tuple[Color, float]]
                            ) -> bool:
    for (bg_color, contrast_ratio) in color_contrast_pairs:
        if text_color.contrast(bg_color) < contrast_ratio:
            return False
    return True
