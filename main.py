import os
from src.some_storage_library import SomeStorageLibrary

def read_source_data(filepath):
    with open(filepath, 'r') as file:
        data = [line.strip().split('|') for line in file]
    return data

def read_source_columns(filepath):
    with open(filepath, 'r') as file:
        columns = [tuple(line.strip().split('|')) for line in file]
    return columns

def write_csv(data, columns, output_filepath):
    sorted_columns = sorted(columns, key=lambda x: int(x[0]))
    column_names = [col[1] for col in sorted_columns[0:]]

    with open(output_filepath, 'w') as file:
        file.write(','.join(column_names) + '\n')
        for row in data:
            file.write(','.join(row) + '\n')

def main():

    source_data_filepath = 'data/source/SOURCEDATA.txt'
    source_columns_filepath = 'data/source/SOURCECOLUMNS.txt'

    data = read_source_data(source_data_filepath)
    columns = read_source_columns(source_columns_filepath)

    output_filepath = 'data/source/output.csv'

    write_csv(data, columns, output_filepath)

    storage_library = SomeStorageLibrary()
    storage_library.load_csv(output_filepath)


if __name__ == '__main__':
    main()
    print('Beginning the ETL process...')