
a =([
    "X.O",
    "XX.",
    "XOO"])
def checkio(game_result: list) -> str:
    for row in game_result:
       if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[1][1] !='.':
       return game_result[0][0]
    elif game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[1][1] !='.':
       return game_result[0][2]
    for i in range(3):
       if game_result[0][i] == game_result[1][i] == game_result[2][i] and game_result[0][i] != '.':
           return game_result[0][i]
    return 'D'

print(checkio(a))