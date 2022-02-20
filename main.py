from fastapi import FastAPI, File, UploadFile, Response
import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/watson/test/")
async def create_upload_file():
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

    the_response = {
        "car_info": {
            "buttons": [
                {
                    "description": "Which car color are you interested in?",
                    "options": color_objects, #type_objects,
                    "response_type": "option",
                    "title": "Car Color"
                }
            ]
        },
        "fromFilter": 1
    }
    return the_response

