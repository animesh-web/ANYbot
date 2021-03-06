from ANYbotGameObject import *


games = []


def get_game(game_id: str, player: dict = None) -> ANYGame:
    for game in games:
        if game.game_id == game_id:
            return game
    games.append(ANYGame(game_id, player))
    return games[-1]


def remove_game(game_id: str) -> bool:
    for index in range(len(games)):
        if games[index].game_id == game_id:
            games.pop(index)
            return True
    return False


def reset_game(game: ANYGame) -> ANYGame:
    temp_game_id = game.game_id
    temp_p1 = game.player2
    temp_p2 = game.player1

    if remove_game(game.game_id):
        games.append(ANYGame(temp_game_id, temp_p1, temp_p2))
        return games[-1]