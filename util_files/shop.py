class Product:
    '''
    Class to represent a product
    ...
    Attributes
    ----------
    name: name of product
    price:price of product
    discount: discount on product in percent
    '''
    def __init__(self,name,price,discount):
        self.name=name
        self.price=price
        self.discount=discount
    
    def getDiscountAmount(self):
        return self.price*self.discount/100
    
    def getDiscountedPrice(self):
        return self.price-self.getDiscountAmount()
    