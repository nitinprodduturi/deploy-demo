import pandas as pd
import numpy as np
import os,sys
from fastapi import FastAPI,File,UploadFile,Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import StreamingResponse

#fastapi

app=FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",tags=["authetication"])
async def index():
    return RedirectResponse(url="docs")

@app.get("/train")
async def train_routes():
    try:
        return {"message": "Hello Nitin"}
    except Exception as e:
        return Response(f"Error Occured! {e}")
    
if __name__ == '__main__':
    app_run(app,host="0.0.0.0",port=8080)