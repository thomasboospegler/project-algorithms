def quick_sort(numbers, start, end):
    if start < end:
        pivot = partition(numbers, start, end)
        quick_sort(numbers, start, pivot - 1)
        quick_sort(numbers, pivot + 1, end)


def partition(numbers, start, end):
    pivot = numbers[end]
    i = start - 1

    for j in range(start, end):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i + 1], numbers[end] = numbers[end], numbers[i + 1]
    return i + 1


def is_anagram(first_string, second_string):
    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    quick_sort(first_string, 0, len(first_string) - 1)
    quick_sort(second_string, 0, len(second_string) - 1)

    first_string = "".join(first_string)
    second_string = "".join(second_string)

    if not first_string or not second_string:
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)
