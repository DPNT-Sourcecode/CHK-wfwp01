

# noinspection PyUnusedLocal
# skus = unicode string
from curses.ascii import isalpha


def skus_validation(skus):
    """skus validation function to ensure correct input"""
    if not isinstance(skus, str):
        return False
    sku_list = skus.split(",")
    if not all([isalpha(sku.strip()) for sku in sku_list]):
        return False
    return True


def checkout(skus):
    if skus_validation(skus):
        pass
    else:
        return -1


