#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:17:50 2023

@author: tristan
"""

# Pour la configuration de la connextion.
# https://docs.streamlit.io/library/advanced-features/configuration
# https://docs.streamlit.io/knowledge-base/deploy/remote-start

# =============================================================================
# Imports et librairies.
# =============================================================================


import streamlit as st

from utils import logger_utils
from utils.url_check import api_call

# Initialize the logger
logger = logger_utils.configure_logger()

# =============================================================================
# Fonction principale.
# =============================================================================


def run():
    """Contains the main page."""
    logger.info('Displaying main page.')

    # Sould always be at the start of the code.
    st.set_page_config(
        page_title="URL Check",
        page_icon="img/artichoke_o.png",
    )

    st.write("# Url Check")
    st.text('')

    st.image('img/artichoke_o.png', width=100)

    str_url = st.text_input(label='Url', placeholder="Enter an URL to check")

    if st.button('Check URL'):

        response = api_call(str_url)
        status = response.status_code
        response_dict = response.json()

        if status == 200:
            if response_dict['char_list']:
                st.warning(f"{response_dict['check_response']}")
                st.warning(f"List of harmful characters : {' '.join(response_dict['char_list'])}")
            else:
                st.success(response_dict['check_response'])
        else:
            st.error(f"There seem to be a problem.\n{api_call}")

    st.text('')
    st.markdown(
        """
        <hr>
        """,
        unsafe_allow_html=True
    )

# =============================================================================
# Starting the program.
# =============================================================================


if __name__ == "__main__":
    run()
