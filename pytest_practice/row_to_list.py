
def row_to_list( row ):
    """
    convert a string with two tabs '\\t' separated values into a list of two strings containing respectve values
    """
    result = row.strip('\n').split('\t')
    if "" in result:
        return
    if len(result) != 2:
        return
    return result

	
