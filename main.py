import pickle

from utils.game import Game


def main():
    start_time = 1682049600  # 2023/04/21 04:00:00
    end_time = 1682294400  # 2023/04/24 00:00:00
    game = Game()
    games = game.fetch_all(start_time=start_time, end_time=end_time)
    pickle.dump(games, open("games.pkl", "wb"))


if __name__ == "__main__":
    main()
