import asyncio
from typing import Final, Union
import os
from dotenv import load_dotenv
from discord import Intents, Client
from RandomColorRoleClient import RandomColorRoleClient


class BasicClient(Client):
    async def on_ready(self):
        print('basic client ready')
        try:
            await self.close()
        except asyncio.CancelledError:
            # bugfix for aiohttp raising undocumented error
            await self.http.close()


def main() -> None:
    load_dotenv()
    TOKEN: Final[Union[str, None]] = os.getenv('DISCORD_TOKEN')

    if not TOKEN:
        print('missing token')
        return

    client: Client = BasicClient(intents=Intents.default())
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
