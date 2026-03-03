# read_movies.py
# Reads all items from the WeirdIceCreamFlavors table and prints them.
# Part of Lab 09 — feature/read-flavors branch

import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "WeirdIceCreamFlavors"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_icecream(cream):
    Flavour = cream.get("Flavour", "Unknown Flavour")
    Calories = cream.get("Calories", "Unknown")
    Type = cream.get("Type", "Unknown")

    print(f"  Flavour  : {Flavour}")
    print(f"  Calories : {Calories}")
    print(f"  Type     : {Type}")

def print_all_icecream():
    """Scan the entire Movies table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No Ice Cream found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} icecream(s):\n")
    for icecream in items:
        print_icecream(icecream)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_icecream()

if __name__ == "__main__":
    main()
