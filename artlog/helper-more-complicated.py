import os
from igdb.wrapper import IGDBWrapper
wrapper = IGDBWrapper("YOUR_CLIENT_ID", "YOUR_APP_ACCESS_TOKEN")

#init vars
categories = ["Type", "Title", "Creator", "Release", "Completion", "Rating"] 
answers = []


art_type = input("What type of art is it?\n1. Film\n2. TV Show\n3. Anime\n4. Book\n5. Manga\n6. Music\n7. Album\n8. Video Game\n")
if art_type == "8":
    print("yup it's a game")