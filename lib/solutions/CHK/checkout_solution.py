

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    sku_list = skus.split(",")
    if not all([isalpha(sku) for sku in sku_list]):
        return -1


