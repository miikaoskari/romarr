from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello"}


@app.get("/games/{game_id}")
async def get_game(game_id):
    return {"game_id": game_id}



