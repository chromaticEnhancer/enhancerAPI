from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from PIL import ImageFilter, Image
import io
import subprocess
from themodel import colorize as colorizer


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/colorise")
async def colorise(image: UploadFile):
    
    with open(f'./images/bw_input.png', 'wb') as img_bw:
        img_bw.write(image.file.read())

    colorizer('./images/')

    return FileResponse("./images/colored/colored_bw_input.png", media_type="image/png")


if __name__== "__main__":

    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
