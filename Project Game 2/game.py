class Vector:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def X(self): return self.X
    def Y(self): return self.Y


class Tile:
    def __init__(self, position, rows, colums):
        # Standard variables
        self.Position = position
        self.Rows     = rows
        self.Columns  = colums
        self.Assets   = 0
        self.Margin   = 2
        self.Size     = 38

        # Climate properties
        self.Climate = None
        self.Desert  = False
        self.Polar   = False
        self.Swamp   = False
        self.Forest  = False
        self.Sea     = False
        self.Mine    = False


        # Tails to next tiles
        self.Up     = None
        self.Down   = None
        self.Left   = None
        self.Right  = None

    def GetClimate(self):
        if self.Desert:
            self.Climate = "desert"
        elif self.Polar:
            self.Climate = "polar"
        elif self.Swamp:
            self.Climate = "swamp"
        elif self.Forest:
            self.Climate = "forest"
        elif self.Mine:
            self.Climate = "mine"
        else:
            self.Climate = "sea"

        return self.Climate


    # Checkt of een variabele None is.
    def NoneCheck(self, var):
        if var == None:
            return False
        else:
            return True

    # Checkt of een tile tussen een aangegeven positie staat.
    def CheckTilePosition(self, min_X, max_X, min_Y, max_Y):
        if self.Position.X >= min_X and self.Position.X <= max_X and self.Position.Y >= min_Y and self.Position.Y <= max_Y:
            return True
        else:
            return False

    # Zoekt op basis van een gegeven x- en y-coördinaat de bijbehorende tile.
    def GetTile(self, x, y):
        tile = self

        while tile.Position.X != x:

            if self.NoneCheck(tile.Right):
                tile = tile.Right
            else:
                self.OutSideOfMapError()
                return tile
        while tile.Position.Y != y:

            if self.NoneCheck(tile.Down):
                tile = tile.Down
            else:
                self.OutSideOfMapError()
                return tile
        return tile

    # Kijkt hoe groot de Tile-array is.
    def ColumsAndRows(self):
        colums  = []
        rows    = []
        columtiles = self
        rowtiles = self
        while columtiles != None:
            columtiles = columtiles.Right
            if columtiles != None:

                colums.append(columtiles)
        while rowtiles != None:
            rowtiles = rowtiles.Down
            if rowtiles != None:
                rows.append(rowtiles)
        return (len(colums), len(rows))

    # Vergelijkbaar met een Map-functie
    def ListTiles(self, tile = None, lst = []):
         for y in range(self.ColumsAndRows()[1]):
             for x in range(self.ColumsAndRows()[0]):
                 tile =self.GetTile(x, y)
                 lst.append(tile)
         return lst


    # Errorhandling
    def OutSideOfMapError(self, message = "The tile you want to get is outside the boundary of this Tile-array"):
        pass#print("Outside of the map!!")

#Method for creating the board.
def create_board(rows, columns):
    _tile       = None
    starttile   = None
    temptile    = None
    above_tiles = None

    for row in range(0, rows):
        for column in range(0, columns):
            _tile = Tile(Vector(column, row),rows, columns)

            # Set climate properties
            if _tile.CheckTilePosition(0, 6, 0, 6):
                if _tile.CheckTilePosition(5, 5, 6, 6) or _tile.CheckTilePosition(6, 6, 6, 6) or _tile.CheckTilePosition(6, 6, 5, 5):
                    _tile.Sea    = True
                else:
                    _tile.Swamp  = True
            elif _tile.CheckTilePosition(11, 17, 0, 6):
                if _tile.CheckTilePosition(11, 11, 5, 5) or _tile.CheckTilePosition(11, 11, 6, 6) or _tile.CheckTilePosition(12, 12, 6, 6):
                    _tile.Sea    = True
                else:
                    _tile.Polar  = True
            elif _tile.CheckTilePosition(0, 6, 11, 17):
                if _tile.CheckTilePosition(5, 5, 11, 11) or _tile.CheckTilePosition(6, 6, 11, 11) or _tile.CheckTilePosition(6, 6, 12, 12):
                    _tile.Sea    = True
                else:
                    _tile.Desert = True
            elif _tile.CheckTilePosition(11, 17, 11, 17):
                if _tile.CheckTilePosition(12, 12, 11, 11) or _tile.CheckTilePosition(11, 11, 11, 11) or _tile.CheckTilePosition(11, 11, 12, 12):
                    _tile.Sea    = True
                else:
                    _tile.Forest = True
            elif _tile.CheckTilePosition(7, 10, 7, 10):
                _tile.Mine     = True
            else:
                _tile.Sea      = True

            # Set tile properties
            if row == 0 and column == 0:
                starttile = _tile
            if column == 0:
                temptile = _tile
            else:
                temptile.Right = _tile
                _tile.Left     = temptile
                temptile       = _tile

            if row > 0:
                _tile.Up         = above_tiles
                above_tiles.Down = _tile
                above_tiles      = above_tiles.Right

        while temptile.Left != None:
            temptile = temptile.Left
        above_tiles = temptile
    return starttile

def tileToPosition(position, offsetx = 285, offsety = 5):
    # Size of one tile
    size = 38

    # Margin between two tiles
    margin = 2

    # Calculate tile position to
    if type(position) == Vector:
        return [(margin + size) * position.X + offsetx, (margin + size) * position.Y + offsety]
    else:
        return [(margin + size) * position]


