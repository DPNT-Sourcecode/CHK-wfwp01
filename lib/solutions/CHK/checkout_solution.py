

# noinspection PyUnusedLocal
# skus = unicode string
from curses.ascii import isalpha


def skus_validation(skus):
    if not isinstance(skus, str):
        return False
    sku_list = skus.split(",")
    if not all([isalpha(sku.strip()) for sku in sku_list]):
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
    if skus_validation(skus):
        return checkout_processor(skus, price_table)
    else:
        return -1




