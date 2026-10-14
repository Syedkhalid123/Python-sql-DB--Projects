import csv
import mysql.connector
from config import DB_CONFIG,FILE_PATH


def read_csv_file(FILE_PATH):
    with open(FILE_PATH,"r",newline="",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        records = []
        for row in reader:
            records.append(row)
    return records

def validate_records(record):
    if not record["customer_id"].strip():
        return False

    try:
        quantity = int(record["quantity"])
        unit_price = float(record["unit_price"])

    except ValueError:
        return False
    
    if quantity <= 0 or unit_price < 0:
        return False
    
    return True

def duplicate_records(records):
    unique_records = []
    seen_ids = set()

    for record in records:
        order_id = record["order_id"]

        if order_id not in seen_ids:
            unique_records.append(record)
            seen_ids.add(order_id)

    return unique_records

sales_data = read_csv_file(FILE_PATH)

valid_records = []
invalid_records = []

for record in sales_data:
    if validate_records(record):
        valid_records.append(record)
    else:
        invalid_records.append(record)
    
unique_records = duplicate_records(valid_records)


print("Total records: ", len(sales_data))
print("Valid records: ", len(valid_records))
print("Invalid records: ", len(invalid_records))
print("Unique records: ", len(unique_records))

for uni_rec in unique_records:
    print("Unique records: ", uni_rec)


#Mysql connection

connection = mysql.connector.connect(**DB_CONFIG)

try:
    if connection.is_connected():
        print("Successfully connected to MySQL!")

except mysql.connector.Error as Error:
    connection.rollback()
    print("Database Error: ", Error)

cursor = connection.cursor()

insert_query = """ insert into sales (order_id, order_date, customer_id, product_name, quantity, unit_price)
                    values(%s, %s, %s, %s, %s, %s)
                """

try:

    for record in unique_records:
        values = (
            int(record["order_id"]),
            record["order_date"],
            record["customer_id"],
            record["product_name"],
            int(record["quantity"]),
            float(record["unit_price"])
        )

        cursor.execute(insert_query,values)

    connection.commit()

    print("Records inserted: ", cursor.rowcount)

finally:
    cursor.close()
    connection.close()