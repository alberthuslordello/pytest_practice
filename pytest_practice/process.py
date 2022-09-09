from .io import read_file, write_file
from preprocessing_helpers import row_to_list, convert_to_int

def preprocess(raw_path, clean_path):
    """
    read file in raw_path remove invalid lines and save result in clean_path.
    invalid lines are lines that don't have:
    - exactly two tab separated numbers
    - integers with comma separating the 1000s
    """
    data = read_file(raw_path)
    clean_data = []
    for line in data:
        line_split = row_to_list()
        if line_split is None:
            continue
        element1 = convert_to_int(line_split[0])
        element2 = convert_to_int(line_split[1])
        if element1 is not None or element2 is not None:
            clean_data.append([element1, element2])
    write_file(clean_path, clean_data)
