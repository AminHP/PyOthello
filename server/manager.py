#python imports
from time import sleep
from random import choice

#project imports
from worldmodel import WorldModel
from connection import Connection
from myparser import Parser
import config


class Manager:
    def __init__(self):
        self.wm = WorldModel()
        self.conn = Connection()


    def init(self):
        self.conn.start_server(port=config.port)
        while len(self.conn.clients) < 2:
            sleep(1)

        white_team_name = self.conn.recv(0, 32)
        self.conn.send(0, b'1')

        black_team_name = self.conn.recv(1, 32)
        self.conn.send(1, b'0')

        self.conn.send(0, black_team_name)
        self.conn.send(1, white_team_name)

        self.conn.set_all_timeouts(5)

        self.wm.init(white_team_name.decode(), black_team_name.decode())


    def run(self):
        sleep(3)

        turn = 1
        while True:
            is_white = bool(turn % 2)
            moved = False
            final_move = None

            try:
                data_bytes = self.conn.recv(0 if is_white else 1, 3)
                if data_bytes:
                    client_turn, move = Parser.decode(data_bytes)
                    if client_turn == turn:
                        if self.wm.check_move(move, is_white):
                            moved = True
                            final_move = move
            except:
                pass

            if not moved:
                print ('random move')
                final_move = choice(self.wm.all_moves(is_white))

            self.wm.do_move(final_move, is_white)
            self.conn.send2all(Parser.encode(turn, final_move))

            w, b = self.wm.result()
            if w + b == 64:
                if w > b:
                    print ('White wins!')
                elif w < b:
                    print ('Black wins!')
                else:
                    print ('Draw!')

            turn += 1
            print (self.wm)
            sleep(1)


        sleep(5)
        self.conn.disconnect()

