

# noinspection PyUnusedLocal
# skus = unicode string
from curses.ascii import isalpha


def checkout(skus):
    if not isinstance(skus, str):
        return -1
    sku_list = skus.split(",").strip(" ")
    if all([isalpha(sku) for sku in sku_list]):
        pass
    else:
        return -1



