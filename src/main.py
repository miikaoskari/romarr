from fastapi import FastAPI, HTTPException
import json
from typing import Optional
from igdb.wrapper import IGDBWrapper

def read_token() -> dict:
    with open("src/token_response.json", "r") as f:
        return json.loads(f.read())
    
token = read_token()

app = FastAPI()


# Serve the API
@app.get("/api")
async def read_api():
    return {"message": "hello"}


@app.get("/api/games")
async def search_games(search: str, limit: int = 20):
    """Query IGDB for games and return JSON results.

    Runs a search for given parameter
    """
    try:
        wrapper = IGDBWrapper(token['client_id'], token['access_token'])

        query = f'search "{search}"; fields id,name,summary,cover.url,first_release_date; limit {limit};'

        byte_array = wrapper.api_request("games", query)
        text = byte_array.decode("utf-8")
        data = json.loads(text)
        return {"count": len(data), "results": data}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/api/add_game")
async def add_game():
    pass
