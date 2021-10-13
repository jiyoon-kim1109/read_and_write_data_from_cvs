# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv


def print_hi():
    dict_from_csv = {}

    # make dictionary from old_reservation_id, new_reservation_id csv file
    with open('Book1.csv', mode='r') as infile:
        reader = csv.reader(infile)
        dict_from_csv = {rows[0]: rows[1] for rows in reader}

    # print(dict_from_csv)

    with open('Book2.csv') as old_cus_rsv_file:
        reader = csv.reader(old_cus_rsv_file)
        old_customer_reservation_id = [rows[0] for rows in reader]
        line_count = len(old_customer_reservation_id)

    print(old_customer_reservation_id)

    with open('Book2.csv', mode='w') as file:
        writer = csv.writer(file)
        for x in old_customer_reservation_id:
            writer.writerow([x, dict_from_csv.get(x)])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
