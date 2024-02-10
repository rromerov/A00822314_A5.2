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


def calculate_total_cost(price_catalogue, sales_record):
    """
    Compute the total cost of sales based on the price catalogue and sales
    records.

    Parameters:
    price_catalogue (list): List of dictionaries containing product
    information.
    sales_record (list): List of dictionaries containing sales
    record information.

    Returns:
    float: Total cost of sales for the given sales record.

    """
    total_cost = 0
    for sale in sales_record:
        product_name = sale.get('Product')
        quantity = abs(sale.get('Quantity'))  # Ensure quantity is positive
        for product in price_catalogue:
            if product.get('title') == product_name:
                unit_price = product.get('price', 0)
                if unit_price < 0:
                    print(f'Warning: Product "{product_name}" has a negative '
                          'price, converting to positive.')
                    unit_price = abs(unit_price)  # Convert to positive
                total_cost += unit_price * quantity
                break
    return total_cost


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

    # Load the price catalogue JSON file
    price_catalogue = load_json(price_catalogue_path)

    if price_catalogue is None:
        print('Error: Failed to load the price catalogue JSON file.')
        return

    with open('SalesResults.txt', 'w', encoding='utf-8') as result_file:
        for sales_record_path in sales_record_paths:
            sales_record = load_json(sales_record_path)
            if sales_record is None:
                print(f'Error: Failed to load the sales record JSON file: '
                      f'{sales_record_path}')
                continue

            # Print the filename of the sales record
            print(f"\nSales record: {sales_record_path}")
            print(f"\nSales record: {sales_record_path}", file=result_file)

            # Calculate the total cost of sales
            total_cost = calculate_total_cost(price_catalogue, sales_record)

            # Print the product information
            table = PrettyTable()
            table.field_names = ["Product", "Quantity",
                                 "Unit Price", "Subtotal"]
            for sale in sales_record:
                product_name = sale.get('Product')
                quantity = sale.get('Quantity')
                if quantity < 0:
                    print(f'Warning: Negative quantity for product:'
                          f'{product_name} found. Converting to positive.')
                    quantity = abs(quantity)  # Convert to positive
                else:
                    quantity = abs(quantity)  # Ensure quantity is positive
                for product in price_catalogue:
                    if product.get('title') == product_name:
                        unit_price = product.get('price', 0)
                        if unit_price < 0:
                            unit_price = abs(unit_price)  # Convert to positive
                        subtotal = unit_price * quantity
                        table.add_row([product_name, quantity,
                                       f"${abs(unit_price):.2f}",
                                       f"${subtotal:.2f}"])
                        break
                else:
                    print(f'Warning: Product: {product_name} not found in the '
                          'price catalogue.')
                    print(f'Warning: Product: {product_name} not found in the '
                          'price catalogue.', file=result_file)
            print(table)
            print(table, file=result_file)

            # Print the total cost of sales
            print(f'Total Cost of Sales: ${total_cost:.2f}')
            print(f'Total Cost of Sales: ${total_cost:.2f}',
                  file=result_file)

            # Print execution time
            print(f'Execution time: '
                  f'{(datetime.now() - start_time).total_seconds():.6f} '
                  'seconds')
            print(f'Execution time: '
                  f'{(datetime.now() - start_time).total_seconds():.6f} '
                  'seconds', file=result_file)


if __name__ == '__main__':
    main()
