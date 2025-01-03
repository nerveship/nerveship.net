from imdb import Cinemagoer
from howlongtobeatpy import HowLongToBeat

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
        counter = 0
        print("What is the Letterboxd URL of the movie?")
        answer = self.ia.get_movie(input())

        # Get directors
        for i in answer['directors']:
            print(str(counter) + ": " + i['name'])
            counter += 1
        print("Which director to list as creator?")
        which_dir = input()
        print(answer['directors'][int(which_dir)])

        # Call format_html with the current type and answer
        format_html(self.type, answer)

    def search_for_game(self):
        print("What is the HowLongToBeat URL of the movie?")
        result = HowLongToBeat().search_from_id(input())
        print(result.game_name)

# External function
def format_html(type, answer):
    print(f"Type: {type}")
    print(f"Answer: {answer}")
    print(answer.year)

classifier = ArtClassifier()
classifier.determine_type()
