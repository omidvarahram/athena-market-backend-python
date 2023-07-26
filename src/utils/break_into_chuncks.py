def sort_data_by_date(data):
    try:
        return sorted(data, key=lambda record: record['timestamp'])
    except (TypeError, KeyError):
        print("Error: Unable to sort data. It is not a valid object")

def break_into_chuncks(data, size):
    sorted_data = sort_data_by_date(data)

    if (sorted_data != None):
        array_of_chunks = [sorted_data[i: i + size] for i in range(0, len(sorted_data), size)]
        print(f"Data succesfully splitted in {size} chunks")
        return array_of_chunks
