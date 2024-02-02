from color_utils import to_discord_color
from random_color_strategies import RandomColor, dark_mode_dominant_strategy
from discord import Client
import asyncio


class RandomColorRoleClient(Client):

    async def on_ready(self) -> None:
        print(f'{self.user} is now running')
        await self._change_role_colors()
        try:
            await self.close()
        except asyncio.CancelledError:
            # bugfix for aiohttp raising undocumented error
            await self.http.close()

    # TODO: put this not in the client class; maybe pass in as a function on the constructor?
    async def _change_role_colors(self):
        # find color of the day roles
        guilds = self.guilds
        random_color_roles = [
            role
            for guild in guilds
            for role in guild.roles
            if role.name.lower() == 'color of the day'
            or role.name.lower() == 'colour of the day'
        ]
        print(f'Guilds: {[role.guild.name for role in random_color_roles]}')

        random_color = RandomColor(dark_mode_dominant_strategy)
        tasks = [
            role.edit(color=to_discord_color(random_color.generate()))
            for role
            in random_color_roles
        ]
        await asyncio.gather(*tasks)
