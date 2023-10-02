#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:55:22 2023

@author: tristan
"""


def check_evil(url):
    """Check evil chars in URL."""

    bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D', '\u1EA1', '\u1EB9']
    result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]

    return result
