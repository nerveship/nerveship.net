import os, constants
from igdb.wrapper import IGDBWrapper

wrapper = IGDBWrapper(constants.client_id, constants.app_access_token)

#init vars
categories = ["Type", "Title", "Creator", "Release", "Completion", "Rating"] 
answers = []


art_type = input("What type of art is it?\n1. Film\n2. TV Show\n3. Anime\n4. Book\n5. Manga\n6. Music\n7. Album\n8. Video Game\n")
if art_type == "8":
    game_title = input("What is the title of the game?\n")

    wrapper.api_request()