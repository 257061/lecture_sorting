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





def main():
    #print(read_data("numbers.csv"))
    data = read_data("numbers.csv")
    data_1 = data["series_1"]
    data_2 = data["series_2"]
    data_3 = data["series_3"]
    print(selection_sort(data_1, "asc"))
    print(selection_sort(data_2, "desc"))
    print(selection_sort(data_3, "asc"))


if __name__ == '__main__':
    main()
