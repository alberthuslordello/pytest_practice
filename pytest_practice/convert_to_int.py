def convert_to_int (value):
    if not isinstance(value, str):
        if isinstance(value, int):
            return value
        else:
            raise TypeError("is not an string or integer")
    return int(value.replace(',', ''))
