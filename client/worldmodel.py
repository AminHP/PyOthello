from part import Part
from move import Move


class WorldModel:
    def __init__(self):
        self.board = [[Part(is_empty=True) for _ in range(8)] for _ in range(8)]
        self.white_team_name = ''
        self.black_team_name = ''
        self.my_color = ''

    def __str__(self):
        res = ''
        for row in self.board:
            for part in row:
                if not part.is_empty:
                    res += ('1' if part.is_white else '-1') + '\t'
                else:
                    res +=  '0\t'
            res += '\n'
        return res


    def init(self, white_name, black_name, my_color):
        self.board[3][3].is_empty = False
        self.board[3][3].is_white = True
        self.board[4][4].is_empty = False
        self.board[4][4].is_white = True

        self.board[3][4].is_empty = False
        self.board[3][4].is_white = False
        self.board[4][3].is_empty = False
        self.board[4][3].is_white = False

        self.white_team_name = white_name
        self.black_team_name = black_name
        self.my_color = my_color

