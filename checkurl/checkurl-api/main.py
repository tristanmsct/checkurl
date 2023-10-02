#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:53:31 2023

@author: tristan
"""

import logging
from logging.config import dictConfig

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from dotenv import dotenv_values

from checker import check_evil

from data_models import UrlData, UrlTarget
from conf import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("check-url")

secrets = dotenv_values('.env')

api_keys = [
    secrets['API_KEY']
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication


def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    """Check the API key for the request."""
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )


app = FastAPI(
    title="Homographic Attack URL Check",
    description="A simple API to check a url for Homographic Attack.",
    version="1",
    contact={
        "name": "Tristan",
        "email": "tristan.muscat@pm.me",
    },
    #openapi_url=None
)


@app.get("/", dependencies=[Depends(api_key_auth)])
def read_root():
    """Landing function."""
    return {"message": "The API is running and ready to check urls."}


@app.post("/api", dependencies=[Depends(api_key_auth)], response_model=UrlTarget)
async def check_url(input_url: UrlData):
    """Check a URL and return a response."""
    str_url = input_url.__dict__['STR_URL']
    logger.info("URL tested : %s", str_url)

    result = check_evil(str_url)

    str_response = "The URL does not seem harmful."
    if result:
        str_response = "The URL seems harmful"

    return {
        'check_response': str_response,
        'char_list': result
    }
