from coloraide import Color
from discord import Colour as DiscordColor


def to_discord_color(color: Color) -> DiscordColor:
    return DiscordColor.from_str(color.to_string(hex=True))


def to_color(discord_color: DiscordColor):
    return Color(
        'srgb',
        [channel / 255.0 for channel in discord_color.to_rgb()]
    )
