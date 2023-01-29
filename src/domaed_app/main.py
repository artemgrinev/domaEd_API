import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.routing import APIRoute
from starlette.requests import Request
from elasticsearch import AsyncElasticsearch
from logging import getLogger, StreamHandler

from db.maps import MAPPING_FOR_PRODUCT, MAPPING_FOR_RECIPES
from db.schemas import CreateProductRequest, GetProductRequest, DeleteIndexRequest, CreateRecipesRequest, \
    GetRecipesRequest

logger = getLogger(__name__)
logger.addHandler(StreamHandler())
logger.setLevel("INFO")


async def ping() -> dict:
    return {"success": True}


async def create_product_index(request: Request) -> dict:
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    await elastic_client.indices.create(index="products", mappings=MAPPING_FOR_PRODUCT)
    return {"success": True}


async def create_recipes_index(request: Request) -> dict:
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    await elastic_client.indices.create(index="recipes", mappings=MAPPING_FOR_RECIPES)
    return {"success": True}


async def delete_product_index(request: Request, index_name: DeleteIndexRequest) -> dict:
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    await elastic_client.indices.delete(index=index_name.name)
    return {"success": True}


async def create_user() -> dict:
    pass


async def create_product(request: Request, body: CreateProductRequest) -> dict:
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.index(index="products", document=body.dict())
    logger.info(res)
    return {"success": True, "result": res}


async def create_recipes(request: Request, body: CreateRecipesRequest):
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.index(index="recipes", document=body.dict())
    logger.info(res)
    return {"success": True, "result": res}


async def update_product():
    pass


async def update_recipes():
    pass


async def update_user():
    pass


async def get_all_product(request: Request):
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.search(index="products", query={"match_all": {}})
    return {"success": True, "result": res}


async def get_product(request: Request, body: GetProductRequest):
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.search(index="products", query={"match": body.dict()})
    return {"success": True, "result": res}


async def get_recipes(request: Request, body: GetRecipesRequest):
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.search(index="recipes", query={"match": body.dict()})
    return {"success": True, "result": res}


async def get_all_recipes(request: Request):
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.search(index="recipes", query={"match_all": {}})
    return {"success": True, "result": res}


routes = [
    APIRoute(path="/ping", endpoint=ping, methods=["GET"]),
    APIRoute(path="/create_product_index", endpoint=create_product_index, methods=["GET"]),
    APIRoute(path="/create_recipes_index", endpoint=create_recipes_index, methods=["GET"]),
    APIRoute(path="/delete_product_index", endpoint=delete_product_index, methods=["GET"]),
    APIRoute(path="/create_product", endpoint=create_product, methods=["POST"]),
    APIRoute(path="/create_recipes", endpoint=create_recipes, methods=["POST"]),
    APIRoute(path="/create_user", endpoint=create_user, methods=["POST"]),
    APIRoute(path="/update_product", endpoint=update_product, methods=["PUT"]),
    APIRoute(path="/update_recipes", endpoint=update_recipes, methods=["PUT"]),
    APIRoute(path="/update_user", endpoint=update_user, methods=["PUT"]),
    APIRoute(path="/get_all_product", endpoint=get_all_product, methods=["POST"]),
    APIRoute(path="/get_all_recipes", endpoint=get_all_recipes, methods=["POST"]),
    APIRoute(path="/get_product", endpoint=get_product, methods=["POST"]),
    APIRoute(path="/get_recipes", endpoint=get_recipes, methods=["POST"]),
]

elastic_client = AsyncElasticsearch()
app = FastAPI()
app.state.elastic_client = elastic_client
app.include_router(APIRouter(routes=routes))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)