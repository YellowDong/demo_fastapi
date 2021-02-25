"""
查询参数
time:2021-02-25 19:43PM
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()
colors = [
    {"item1": "yellow"},
    {"item2": "blue"},
    {"item3": "red"}
]

# 访问http://127.0.0.1:8000/items/或http://127.0.0.1:8000/items/?skip=0&limit=10效果一致
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return colors[skip: skip + limit]


# 可选参数
# item_id 为路径参数
from typing import Optional

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None ):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 多个路径参数和查询参数
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

# 必须查询参数
# needy 为必须查询参数要访问http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

if __name__ == '__main__':
    uvicorn.run(app)


