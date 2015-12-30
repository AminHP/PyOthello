# python imports
from struct import pack, unpack

# project imports
from move import Move

class Parser:
    @staticmethod
    def decode(data):
        data = unpack('HB', data)
        return data[0], Move(data[1] % 8, data[1] // 8)

    @staticmethod
    def encode(turn, move):
        p = move.y * 8 + move.x
        return pack('HB', turn, p)
