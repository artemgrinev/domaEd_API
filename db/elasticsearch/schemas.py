from datetime import date

from pydantic import BaseModel


class CreateProductRequest(BaseModel):
    name: str
    category: str
    market_name: str
    url: str
    product_id: int
    price: float
    manufacturer: str
    amount: float
    measure: str
    update_date: date


class GetProductRequest(BaseModel):
    name: str


class GetRecipesRequest(BaseModel):
    name: str


class DeleteIndexRequest(BaseModel):
    name: str


class CreateRecipesRequest(BaseModel):
    name: str
    ingredients: list
    url: str
    resource: str
    create_date: date
    update_date: date
