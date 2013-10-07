from tetris import Controllable, Visible


class Tetromino(Controllable, Visible):
    '''There are 7 different tetromino possible:
    O-Shape:
    ['     ']
    xx
    xx

    L-Shape & J-Shape:
    xxx     xxx
      x     x

    T-Shape:
    xxx
     x

    S-Shape & Z-Shape:
    xx      xx
     xx    xx

    I-Shape:
    xxxx

    Each shape is 4 blocks and all rotation options fit into a 5x5 grid
    '''
    O_SHAPE = [
        ['     '],
        ['  xx '],
        ['  xx '],
        ['     '],
        ['     ']
    ]

    PIECES = {
        'O': O_SHAPE
    }
