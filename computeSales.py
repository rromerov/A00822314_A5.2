# pylint: disable=invalid-name
"""
computeSales.py

This script calculates the total cost of sales based on a price catalogue
and a sales record provided as JSON files.

Usage:
    python computeSales.py priceCatalogue.json salesRecord.json

The script takes two arguments:
    - priceCatalogue.json: JSON file containing information about product
    prices.
    - salesRecord.json: JSON file containing records of sales.

The script then computes the total cost of all sales recorded in
salesRecord.json, using the prices from priceCatalogue.json, and outputs
the result to the console and to a file named SalesResults.txt.
"""
import json
import sys
from datetime import datetime


def load_json(file_path):
    """
    Load JSON data from a file.

    Parameters:
    file_path (str): Path to the JSON file.

    Returns:
    dict: JSON data loaded from the file.

    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading {file_path}: {e}')
        return None


def compute_total_cost(price_catalogue, sales_record):
    """
    Compute the total cost of sales based on the price catalogue and sales
    record.

    Parameters:
    price_catalogue (list): List of dictionaries containing product
    information.
    sales_record (list): List of dictionaries containing sales record
    information.

    Returns:
    float: Total cost of all sales.

    """
    total_cost = 0
    for sale in sales_record:
        product_name = sale.get('Product')
        quantity = sale.get('Quantity')
        for product in price_catalogue:
            if product.get('title') == product_name:
                total_cost += product.get('price', 0) * quantity
                break
    return total_cost


def main():
    """
    Main function to execute the program.
    """
    if len(sys.argv) != 3:
        print('Incorrect usage. Please provide two JSON files as arguments')
        return

    start_time = datetime.now()

    price_catalogue_path = sys.argv[1]
    sales_record_path = sys.argv[2]

    price_catalogue = load_json(price_catalogue_path)
    sales_record = load_json(sales_record_path)

    if price_catalogue is None or sales_record is None:
        print('Error: Failed to load one or both of the JSON files.')
        return

    total_cost = compute_total_cost(price_catalogue, sales_record)

    execution_time = datetime.now() - start_time

    sales = f'Total cost of sales: ${total_cost:.2f}'

    time = f'Execution time: {execution_time.total_seconds():.6f} seconds'

    end_result = f'{sales}\n{time}'

    print(end_result)

    with open('SalesResults.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(end_result)


if __name__ == '__main__':
    main()
