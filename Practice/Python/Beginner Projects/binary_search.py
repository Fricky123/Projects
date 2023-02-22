a = [1, 123, 12, 234, 432, 23, 43, 2234, 432, 234, 341, 123, 123, 12123, 4241, 999999]
b = [1, 2, 3, 4, 5]

def binary_search(sorted_list, chosen_value, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(sorted_list) - 1

    mid = (low + high) // 2

    if chosen_value == sorted_list[mid]:
        return mid

    elif chosen_value > sorted_list[mid]:
        binary_search(sorted_list, chosen_value, mid + 1, high)

    elif chosen_value < sorted_list[mid]:
        binary_search(sorted_list, chosen_value, low, mid - 1)

number = binary_search(b, 2)

print(number)
