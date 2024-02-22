import aiohttp, asyncio
from phone import Phone
from cst import *


class Network:
    def __init__(self) -> None:
        self.phones = [Phone(ID) for ID in ID_LUT]

    async def execute_async(self, func: function, **func_kwargs):
        async with aiohttp.ClientSession() as session:

            for phone in self.phones:
                phone.session = session
                try:
                    await func(phone, func_kwargs)
                except:
                    print(f"[{phone.id}] >> Connexion error")
        return None
