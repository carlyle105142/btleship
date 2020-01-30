class Board(object):
    def __init__(self, row: int, col: int) -> None:
        self.content = [['*' for c in range(col)] for r in range(row)]


    def row_num(self):
        return len(self.content)

    def col_num(self):
        return len(self.content[0])

    def __str__(self):
        display = '  '+' '.join([str(n) for n in range(self.col)])+'/n'
        for row_num, row in enumerate(self):
            display += str(row_num)+' '+' '.join(row for c in col_num) + '/n'
        return display

    def __iter__(self):
        return iter(self.content)

    def __getitem__(self, item: int) -> list:
        # returns the specific row indexed at [item]
        return self.content[item]


class Ship(object):
    def __init__(self, ship_type: str, size:int, orientation: str, position: str) -> None:
        self.ship_type = ship_type
        self.size = size
        self.orientation = orientation
        self.position = position

    def get_ship_size(self) -> int:
        return self.size

    def direction(self) -> str:
        if self.orientation in 'vertical':
            return 'vertical'
        elif self.orientation in 'horizontal':
            return 'horizontal'

    def notation(self) -> str:
        return self.ship_type[0]

    def get_position(self) -> tuple:
        coordinate = [i for i in self.position.split(',')]
        hor_pos = coordinate[0]
        ver_pos = coordinate[1]
        return hor_pos,ver_pos
    def verify_pos_range(self) -> bool:
        if self.get_position()[0] not in range(Board.col) or self.get_position()[1] not in range(Board.row):
            print("Cannot place %s %s at %d, %d because it would be out of bounds." % (self.ship_type, self.direction(), self.get_position()[0],self.get_position()[1]))
            return False

    def verify_ship_range(self) -> bool:
        coord_int = [i for i in self.position.split(',')]
        if direction() is 'vertical':
            if self.get_position()[0] not in range(Board.row + 1 - self.get_ship_size()):
                print("Cannot place %s %s at %d, %d because it would end up out of bounds." % (self.ship_type, self.direction(), self.get_position()[0],self.get_position()[1]))
                return False
        elif direction() is 'horizontal':
            if self.get_position()[1] not in range(Board.col + 1 - self.get_ship_size()):
                print("Cannot place %s %s at %d, %d because it would end up out of bounds." % (self.ship_type, self.direction(), self.get_position()[0],self.get_position()[1]))
                return False
        else:
            return True

    def verify_input(self) -> bool:
        coord_int = [i for i in self.position.split(',')]
        if len(coord_int) != 2:
            print("Please enter two digits as starting coordinate of the ship")
            return False
        if type(coordint[0]) != int:
            print("Please enter integer as coordinate number")
            return False
        if























if __name__ == '__main__':
    pass

