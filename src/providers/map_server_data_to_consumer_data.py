from utils.conversion.convert_date_time_to_iso_timestamp import convert_date_time_to_iso_timestamp as convertor
def map_mt4_historical_to_raw(mt4_json, symbol_string, timeframe_number):

    newData = {"data": []}

    for candle in mt4_json["data"]:
        newCandle = {
            **candle,
            "symbol": symbol_string,
            "timefram": timeframe_number,
            "timestamp": convertor(candle["date"], candle["time"])
        }
        newCandle.pop('time', None),
        newCandle.pop('date', None)

        newData["data"].append(newCandle)


    return newData