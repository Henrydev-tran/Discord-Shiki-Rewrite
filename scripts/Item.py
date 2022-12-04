class _vitem:
    def __init__(self, name, price, sellingprice, description, rarity, type, id, reusable, reusecount=0):
        self.name = name
        self.price = price
        self.sellingprice = price
        self.description = description
        self.rarity = rarity
        self.type = type
        self.id = id
        self.reusable = reusable
        self.reusecount = reusecount

    def JSONstringable(self, amount):
        return [self.name, str(amount), self.reuseable]

