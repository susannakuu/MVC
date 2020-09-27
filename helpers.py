import exceptions
from product import Product

# repsresents shop structure
# list of Product type objects
items = []

# add item to items
def addItem(name, price, amount):
    global items
    # create product with reqiure description
    product = Product(name, price, amount)
    # control is item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        items.append(product)
# show items
def showItems():
    global items
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return items
# show item
def showItem(name):
    global items
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Not found {} item".format(name))
# delete item
def deleteItem(name):
    global items
    isDeleted = False
    for item in items:
        # if the name is the same as we search
        if (item.getName() == name):
            items.remove(item)
            isDeleted = True
        else:
            continue
    if (isDeleted != True):
        raise exceptions.ItemNotExists("Not found {} item.".format(name))
# delete all items
def deleteAllItems():
    global items
    items.clear()
# update items price and amount
def updateItem(name, price, amount):
    global items
    isUpdated = False
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            # update item
            item.setPrice(price)
            item.setAmount(amount)
            isUpdated = True
        else:
            continue
    if (isUpdated != True):
        raise exceptions.ItemNotExists("Not found {} item".format(name))
