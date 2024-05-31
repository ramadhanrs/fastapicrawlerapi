import uvicorn
from fastapi import FastAPI
from crawler import crawler

app = FastAPI()

@app.get("/")
async def test():
    return {"hello":"world"}

@app.post("/crawler_all/")
async def test(url:str):
    value = crawler.get_links_from_urls(url) 
    return value

@app.post("/crawler/")
async def test(url:str):
    value = crawler.get_links_from_url_singel_page(url) 
    return value