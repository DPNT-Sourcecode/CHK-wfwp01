

# noinspection PyUnusedLocal
# skus = unicode string
from curses.ascii import isalpha


def checkout(skus):
    if not isinstance(skus, str):
        return -1
    else:
        pass
    sku_list = skus.split(",")
    if all([isalpha(sku.strip()) for sku in sku_list]):
        pass
    else:
        return -1
