from imdb import Cinemagoer
from howlongtobeatpy import HowLongToBeat

which_dir = int()

class ArtClassifier:
    def __init__(self):
        self.type = ""
        self.ia = Cinemagoer()

    def determine_type(self):
        print("What type of art is it?")
        self.type = input()

        if self.type.strip().lower() == "film":
            self.search_for_film()
        elif self.type.strip().lower() == "game":
            self.search_for_game()

    def search_for_film(self):
        print("What is the IMDB ID of the movie?")
        answer = self.ia.get_movie(input())

        # Call format_html with the current type and answer
        format_html(self.type, answer)

    def search_for_game(self):
        print("What is the HowLongToBeat URL of the movie?")
        result = HowLongToBeat().search_from_id(input())
        print(result.game_name)

# External function
def format_html(type, answer):
    print(f"Type: {type.capitalize()}")
    print(f"Title: {answer}")

classifier = ArtClassifier()
classifier.determine_type()
