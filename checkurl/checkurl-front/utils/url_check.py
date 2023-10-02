#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:25:34 2023

@author: tristan
"""

import requests
from dotenv import dotenv_values

secrets = dotenv_values('.env')


def api_call(str_url):
    """Call the API with the URL to check."""
    headers = {
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Authorization': f"Bearer {secrets['API_KEY']}",
    }

    json_data = {
        'STR_URL': str_url,
    }

    response = requests.post('https://checkurl-api.datartichaut.com/api', headers=headers, json=json_data)

    return response
