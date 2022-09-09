""" 
Read and write data files
"""

def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return lines


def write_file(path, data):
    with open(path, "w") as f:
        for line in data:
            f.write(str(line[0]) + '\t' + str(line[1]))
