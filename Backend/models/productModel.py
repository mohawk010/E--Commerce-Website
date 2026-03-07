from pydantic import BaseModel,Field

from enum import Enum
from typing import Optional
from datetime import datetime
class ProductCategory(str,Enum):
    ELECTRONICS = 'Electronics'
    FASHION = 'Fashion'
    ACCESSORIES = 'Accessories'
    HOME = 'Home & Kitchen'
    BEAUTY = 'Beauty & Personal Care'

class Product(BaseModel):
    title:str =Field(...)
    description:str = Field(...)
    price:int = Field(...)
    category:Optional[ProductCategory] = Field(...) 
    created_at:datetime =  Field(default_factory=datetime.now)
    updated_at:datetime =  Field(default_factory=datetime.now)