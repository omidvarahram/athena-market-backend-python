from providers.prepare_data import prepare_data
import asyncio

asyncio.run(prepare_data("AUDUSD", "m5"))
