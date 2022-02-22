from fastapi import FastAPI, File, UploadFile, Response
import pandas as pd
from pydantic import BaseModel

class Item(BaseModel):
    distinct: str

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/watson/test/")
async def create_upload_file(item: Item):
    # print('hii')
    # print(item.distinct)
    df = pd.read_csv("dataframe.csv")
    color_ls = df.Color
    type_ls = df.Type
    color_objects = []
    type_objects = []

    for color in color_ls:
        color_template = {
            "label": color,
            "value": {
                "input": {
                    "text": color
                }
            }
        }
        color_objects.append(color_template)

    for type in type_ls:
        type_template = {
            "label": type,
            "value": {
                "input": {
                    "text": type
                }
            }
        }
        type_objects.append(type_template)

    print(color_objects + type_objects)

    if item.distinct == 'color':
        response_object = color_objects
    elif item.distinct == 'type':
        response_object = type_objects
    else:
        response_object = type_objects + color_objects

    the_response = {
        "car_info": {
            "buttons": [
                {
                    "description": "Which car color are you interested in?",
                    "options": response_object,
                    "response_type": "option",
                    "title": "Car Color"
                }
            ]
        },
        "fromFilter": 1
    }
    return the_response

