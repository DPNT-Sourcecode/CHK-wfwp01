

# noinspection PyUnusedLocal
# skus = unicode string
from curses.ascii import isalpha
from collections import Counter


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

def special_offer_processor(sku_list, price_table):
    sku_list_counts = Counter(sku_list)
    special_offer_skus = ["A", "B"]
    special_offer_discount = 0
    for sku in special_offer_skus:
        if sku == A:
            special_offer_discount += sku_list_counts[sku] // 3 * 20
        if sku == B:
            special_offer_discount += sku_list_counts[sku] // 3 * 20



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


