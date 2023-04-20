
import csv
def main():
    key_column_index = [0]
    filename = "product.csv" 
    products_dict = read_dictionary(filename, key_column_index)

    # Print the dentists compound dictionary.
    print(products_dict)




def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty dictionary that will
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.

    filename = "products.csv"

    with open(filename, "rt") as csv_file:
        read = csv.reader(csv_file)
        next (read)


        #If the current row is not blank, add the
        # data from the current to the dictionary.
        for key_column_index in read:
         product_number = key_column_index[0]
         product_name = key_column_index [1]
         price =  key_column_index[2]
         dictionary[product_number] = [product_number, product_name, price]
    

    request_list = []    
    with open("request.csv", "rt") as csv_file:
        check = csv.reader(csv_file)
        next (check)

        for key_column_index in check:
            product_num = key_column_index[0]
            quatity = key_column_index[1]
            request_list = [product_num, quatity]

    print("request items")

    for request_list in dictionary:
        value = dictionary[request_list]
        product_name = value[1]
        price = value[2]
        print(f"{product_name}: {quatity} @ {price}")



if __name__ == "__main__":
    main()