from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True

product_one = Product(id = 1, name = 'sahil', price=100, in_stock=False)

print(product_one)