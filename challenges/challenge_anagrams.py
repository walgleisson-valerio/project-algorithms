# função de ordenação baseada nos estudos dp que foi ensinado na trybe, e numa questão respondida no stackoverflow (https://stackoverflow.com/questions/13101468/python-how-to-sort-the-alphabet-in-a-list-without-sorted-functions), no qual eu reolvi reimpplentar para ficar mais didático.
def quicksort(string):
    if len(string) == 0:
        return string

    pivot = string[0]
    left_string = [x for x in string[1:] if x <  pivot]
    right_string = [x for x in string[1:] if x >= pivot]

    ordered_left_string = quicksort(left_string)
    ordered_right_string = quicksort(right_string)

    return (
        "".join(ordered_left_string)
        + pivot
        + "".join(ordered_right_string)
    )


def is_anagram(first_string, second_string):
    ordered_first_string = quicksort(first_string.lower())
    ordered_second_string = quicksort(second_string.lower())

    if len(first_string) == 0 or len(second_string) == 0:
        return (ordered_first_string, ordered_second_string, False)

    return (
        ordered_first_string,
        ordered_second_string,
        ordered_first_string == ordered_second_string
    )