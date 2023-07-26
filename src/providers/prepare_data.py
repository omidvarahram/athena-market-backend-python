import json
import asyncio

from providers.map_server_data_to_consumer_data import map_mt4_historical_to_raw
from providers.config_manager import getConfigByKey
from utils.break_into_chuncks import break_into_chuncks

async def prepare_data(symbol_string, timeframe_string):
    mt4_data_path = getConfigByKey("data__mt4_path");
    db_path = getConfigByKey("database_path");
    with open(f"{mt4_data_path}database.json", "r") as json_file:
        data = json.load(json_file)

        transformed_data = map_mt4_historical_to_raw(data, symbol_string, timeframe_string)
        print("Data successfully mapped.")

        if len(transformed_data["data"]) != 0:
            chunked_data = break_into_chuncks(transformed_data["data"], 1000)
            index = 0
            for chunck in chunked_data:
                index += 1
                start_date = chunck[0]["timestamp"]
                end_date = chunck[len(chunck) - 1]["timestamp"]
                newData = {
                    "data": {
                        "start_date": start_date,
                        "end_date": end_date,
                        "candles": chunck
                    }
                }
                with open(f"{db_path}db_{symbol_string}_{timeframe_string}_{index}.json", "w") as json_file:
                    json.dump(newData, json_file, indent=4)
                    print("Data successfully stored in database.")