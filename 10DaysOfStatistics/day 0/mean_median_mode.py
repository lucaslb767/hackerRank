# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean_median_mode(arr):
    size = len(arr)
    mean = round(sum(arr) / size, 1)
    sorted_array = sorted(arr)
    mode = ''
    median = 0
    if (size % 2 == 0):
        median = round((sorted_array[size // 2 - 1] + sorted_array[size // 2]) / 2, 1)
    else:
        median = sorted_array[((size - 1) / 2) + 1]

    unique_elements = set(sorted_array)

    dictionary_elements_frequency = {}

    for value in unique_elements:
        dictionary_elements_frequency.update({value: 0})

    for element in sorted_array:
        if (element in dictionary_elements_frequency):
            dictionary_elements_frequency[element] += 1

    biggest_value = -2
    mode = ''

    for k, value in dictionary_elements_frequency.items():
        if (value == biggest_value):
            if (int(k) < int(mode)):
                mode = k
        elif (value > biggest_value):
            biggest_value = value
            mode = k

    print(mean)
    print(median)
    print(mode)


if __name__ == '__main__':
    size = int(input())
    a = list(map(int, input().split()))
    mean_median_mode(a)