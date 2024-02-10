# pylint: disable=invalid-name
"""
computeSales.py

This script calculates the total cost of sales based on a price catalogue
and one or multiple sales records provided as JSON files.

Usage:
    python computeSales.py priceCatalogue.json salesRecord.json

The script takes multiple arguments:
    - priceCatalogue.json: JSON file containing information about product
    prices.
    - salesRecord.json: JSON file containing information about sales records.

The script then computes the total cost of all sales recorded in each
salesRecord JSON file, using the prices from priceCatalogue.json, and
outputs the result to the console and to a file named SalesResults.txt.
"""
import json
import sys
from datetime import datetime
from prettytable import PrettyTable


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


def calculate_total_cost(price_catalogue, sales_records):
    """
    Compute the total cost of sales based on the price catalogue and sales
    records.

    Parameters:
    price_catalogue (list): List of dictionaries containing product
    information.
    sales_records (list): List of lists of dictionaries containing sales
    record information.

    Returns:
    dict: A dictionary containing the total cost of sales for each sales
    record file.

    """
    total_costs = {}
    for i, sales_record in enumerate(sales_records, start=1):
        total_cost = 0
        for sale in sales_record:
            product_name = sale.get('Product')
            quantity = sale.get('Quantity')
            for product in price_catalogue:
                if product.get('title') == product_name:
                    total_cost += product.get('price', 0) * quantity
                    break
        total_costs[f'SalesRecord{i}.json'] = total_cost
    return total_costs


def main():
    """
    Main function to execute the program.
    """
    if len(sys.argv) < 3:
        print('Incorrect usage. Please provide at least two JSON files as '
              'arguments')
        return

    start_time = datetime.now()

    price_catalogue_path = sys.argv[1]
    sales_record_paths = sys.argv[2:]

    price_catalogue = load_json(price_catalogue_path)
    sales_records = [load_json(path) for path in sales_record_paths]

    if price_catalogue is None or None in sales_records:
        print('Error: Failed to load one or both of the JSON files.')
        return

    total_costs = calculate_total_cost(price_catalogue, sales_records)

    execution_time = datetime.now() - start_time

    table = PrettyTable()
    table.field_names = ["File", "Total Cost of Sales"]
    for file_name, total_cost in total_costs.items():
        table.add_row([file_name, f"${total_cost:.2f}"])

    print(table)
    print(f'Execution time: {execution_time.total_seconds():.6f} seconds')

    with open('SalesResults.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(str(table))
        result_file.write(f'Execution time: '
                          f'{execution_time.total_seconds():.6f} seconds')


if __name__ == '__main__':
    main()
