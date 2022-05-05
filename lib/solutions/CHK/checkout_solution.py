

# noinspection PyUnusedLocal
# skus = unicode string
from curses.ascii import isalpha


def skus_are_valid(skus):
    if not isinstance(skus, str):
        return False
    sku_list = [sku.strip() for sku in skus.split(",")]
    if not all([isalpha(sku) for sku in sku_list]):
        return False
    return True


price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}


def checkout_processor(sku_list, price_table):
    total = 0
    for sku in sku_list:
        total += price_table[sku.upper()]
    return total


def checkout(skus):
    if skus_are_valid(skus):
        sku_list = [sku.strip() for sku in skus.split(",")]
        return checkout_processor(sku_list, price_table)
    else:
        return -1
