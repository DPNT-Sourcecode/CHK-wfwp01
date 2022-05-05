# noinspection PyUnusedLocal
# skus = unicode string
from curses.ascii import isalpha
from collections import Counter

price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}


def sku_list_builder(skus):
    sku_list = []
    for char in skus:
        if isalpha(char):
            sku_list.append(char.upper())
    return sku_list


def skus_are_valid(skus):
    if not isinstance(skus, str):
        return False
    if len(skus) == 0:
        return False
    if isinstance(skus, str) and len(skus) == 1:
        if not all([isalpha(sku) for sku in skus]):
            return False
    else:
        if not all([isalpha(sku.strip()) for sku in skus.split(",")]):
            return False
    return True


def special_offer_processor(sku_list):
    sku_list_counts = Counter(sku_list)
    special_offer_skus = ["A", "B"]
    special_offer_discount = 0
    for sku in special_offer_skus:
        if sku == "A":
            special_offer_discount += sku_list_counts[sku] // 3 * 20
        if sku == "B":
            special_offer_discount += sku_list_counts[sku] // 3 * 15
    return special_offer_discount


def checkout_processor(sku_list, price_table):
    total = 0
    for sku in sku_list:
        total += price_table[sku.upper()]
    total -= special_offer_processor(sku_list)
    return total


def checkout(skus):
    if skus_are_valid(skus):
        sku_list = sku_list_builder(skus)
        return checkout_processor(sku_list, price_table)
    else:
        return -1





