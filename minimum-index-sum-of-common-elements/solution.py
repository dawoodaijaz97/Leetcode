def solve(list1: list, list2: list) -> int:
    """
    Finds the minimum index sum of common elements between two lists.
    
    :param list1: First list of strings.
    :param list2: Second list of strings.
    :return: Minimum index sum of common elements.
    """
    index_sum = float('inf')
    common_elements = set(list1) & set(list2)
    
    for element in common_elements:
        current_sum = list1.index(element) + list2.index(element)
        if current_sum < index_sum:
            index_sum = current_sum
    
    return index_sum