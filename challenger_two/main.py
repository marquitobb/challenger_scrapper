from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from filter_selenium import JumboScraper

app = FastAPI()


class URLRequest(BaseModel):
    url: str = Field(description="URL to scrape products", example="https://www.tiendasjumbo.co/supermercado/despensa/aceite")

class ResponseProducts(BaseModel):
    products: list = Field(description="List of products", example=[{"name": "product_name", "price": "product_price", "promo_price": "product_promo_price"}])
    url: str = Field(description="URL used to scrape products", example="https://www.tiendasjumbo.co/supermercado/despensa/aceite")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post(
    "/scrape-products/",
    response_model=ResponseProducts,
)
def scrape_products(request: URLRequest):
    scraper = JumboScraper()
    products = scraper.scrape_products(request.url)
    response_products = ResponseProducts(products=products, url=request.url)
    scraper.close()
    return response_products