import pickle

from utils.game import Game


def main():
    game = Game()
    games = game.fetch_all()
    pickle.dump(games, open("games.pkl", "wb"))


if __name__ == "__main__":
    main()
