from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from PIL import ImageFilter, Image
import io

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
    image_data = await image.read()

    image_object = Image.open(io.BytesIO(image_data))
    blurred_image = image_object.filter(ImageFilter.GaussianBlur(radius=10))
    blurred_image.save("newfile.jpeg",)

    return FileResponse("newfile.jpeg", media_type="image/jpeg")
