import asyncio
from providers.prepare_data import prepare_data

asyncio.run(prepare_data("AUDUSD", "m5"))
