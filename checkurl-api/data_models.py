#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:55:54 2023

@author: tristan
"""

from pydantic import BaseModel


class UrlData(BaseModel):
    """Model for the input data."""
    STR_URL: str


class UrlTarget(BaseModel):
    """Model for the output data."""
    check_response: str
    char_list: list
