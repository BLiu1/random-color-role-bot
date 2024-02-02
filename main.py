from typing import Final, Union
import os
from dotenv import load_dotenv
from discord import Intents, Client
from RandomColorRoleClient import RandomColorRoleClient


def main() -> None:
    load_dotenv()
    TOKEN: Final[Union[str, None]] = os.getenv('DISCORD_TOKEN')

    if not TOKEN:
        print('missing token')
        return

    client: Client = RandomColorRoleClient(intents=Intents.default())
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
