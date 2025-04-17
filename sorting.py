import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        data = {"series_1":[], "series_2":[], "series_3":[]}
        for row in reader:
            #print(row)
            for key, value in row.items():   #iterace přes slovník -> přes klíče
                data[key].append(int(value))
    return data


# SELECTION SORT - nestabilní
def selection_sort(numbers, direction):
    n = len(numbers)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_idx] and direction == "asc":
                min_idx = j
            elif numbers[j] > numbers[min_idx] and direction == "desc":
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers


# BUBBLE SORT - stabilní
def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(n-i-1):
            # pokud má první prvek větší hodnotu než prvek druhý -> prohodíme jejich pořadí
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


# INSERTION SORT
def insertion_sort(numbers):
    n = len(numbers)

    for i in range(1, n):
        key = numbers[i]   # první prvek z neseřazené oblasti
        j = i-1   # předchůdce key

        while j >= 0 and key < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = key

    return numbers


# VYZKOUŠEJ A ANALYZUJ VÝSTUP
my_list = [3, 8, 1, 2, 32]
my_list.sort()
print(my_list)   #[1, 2, 3, 8, 32]

my_list = [3, 8, 1, 2, 32]
my_list = sorted(my_list)
print(my_list)  #[1, 2, 3, 8, 32]

my_list = sorted(my_list, reverse=True)

list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=len)
print(list_of_words)   #['MOO', 'woof', 'meeeoow', 'BZZZZZZ']

list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=str.lower)
print(list_of_words)   #['BZZZZZZ', 'meeeoow', 'MOO', 'woof']





def main():
    #print(read_data("numbers.csv"))
    data = read_data("numbers.csv")
    data_1 = data["series_1"]
    data_2 = data["series_2"]
    data_3 = data["series_3"]
    #print(selection_sort(data_1, "asc"))
    #print(selection_sort(data_2, "desc"))
    #print(selection_sort(data_3, "asc"))

    #print(bubble_sort(data_1))
    #print(bubble_sort(data_2))
    #print(bubble_sort(data_3))

    print(insertion_sort(data_1))
    print(insertion_sort(data_2))
    print(insertion_sort(data_3))


if __name__ == '__main__':
    main()
