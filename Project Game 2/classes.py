class Board:
    def __init__(self, starttile, players):
        self.players = players
        self.assets = []
        self.current_player = None
        self.tiles = starttile
        self.turnsLeft = 4
        
        

    def endTurn(self):
        currentPlayerIndex = self.players.index(current_player)
      
        if currentPlayerIndex + 1 > (len(self.assets) - 1):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[currentPlayerIndex + 1]
        

class Player:
    def __init__(self,name):
        self.name = name
        self.money = 500
        
        self.turn = 4
        self.assets = []

    def current_player(self):
        random.shuffle(players)
        for player in players:
            player = self.current_player
            if self.player == self.current_player:
                
                for asset in self.assets:
                    self.money += 150
                """
                for x in self.turn:
                    if self.player:
                        self.boat()
                        self.turn -= 1
                    elif self.player:
                        self.tank()
                        self.turn -= 1
                    elif self.player:
                        self.boat()
                        self.turn -= 1
                        for move in map:
                            self.turn -= 1"""
                    

    def current_player_message(self):
        font = pygame.font.SysFont("monospace", 20)
        text = font.render("Current player is:" + self.current_player, 1, white)
        startDisplay.blit(text, (710, 10))




class Assets():
    def __init__(self, asset, image, position, life, damage):
        self.asset = asset     
        self.image = image
        self.position = position
        self.life = life
        self.damage = damage

    def soldier(self):
        self.soldier = False
        if self.soldier == True:
            startDisplay.blit(player1,(0,39))
            self.money -= 150
            self.life = 50
            self.damage = range(30,70)

    def boat(self):
        self.boat = False
        if self.buy_boat == True:
            #startDisplay.blit(boat1,())
            self.money -= 350
            self.life = 200
            self.damage = range(150,250)
                       
    def tank(self):
        self.boat = False
        if self.buy_boat == True:
            self.money -= 500
            self.life = 300
            self.damage = range(200,350)

 
