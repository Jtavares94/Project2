from Frequency import *

class Node:
  def __init__(self, value, tail):
    self.Tail = tail
    self.Value = value
    self.IsEmpty = False

class Empty: 
  def __init__(self):
    self.IsEmpty = True
  def __str__(self):
      return ""
  def draw(self, offset, screen, texture):
      return None
  def reset (self):
      return None 

Empty = Empty()


class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def __str__(self):
        return "(" + str(self.X) + "," + str(self.Y) + ")"

class Player:
    def __init__(self,name,player):
        self.name = name
        self.money = 500
        self.player = player

#players
player1 = Player("p1","player1")
player2 = Player("p2","player2")
player3 = Player("p3","player3")
player4 = Player("p3","player4")

players = [player1, player2, player3, player4]

class gamestate(Player, Frequency):
    def __init__(self, current, player):
        self.player = player
        self.current_player = current
        self.turn = 4
        self.money = 500 

    def soldier(self):
        self.soldier = False
        if self.soldier == True:
            startDisplay.blit(player1,(player1pos[0]*(L+d),player1pos[1]*(L+d)))
            self.money -= 150

    def boat(self):
        self.boat = False
        if self.buy_boat == True:
            #startDisplay.blit(boat1,(boat1pos[0]*(L+d),boat1pos[1]*(L+d)))
            self.money -= 350
            w
    def tank(self):
        self.boat = False
        if self.buy_boat == True:
            self.money -= 500

    def current_player(self):
        if self.player == self.current_player:
            self.money += 150
            self.turn = 4
            for x in self.turn:
                if self.player:
                    self.boat()
                    self.turn -= 1
                if self.player:
                    self.tank()
                    self.turn -= 1
                if self.player:
                    self.boat()
                    self.turn -= 1


            
            


        

        

             



class Frequency(object):
    def __init__(self, name, life, texture, playerid, HomeBase, damage, price):
        self.name = name
        self.life = life
        self.texture = texture
        self.playerID = playerid
        self.HomeBase = HomeBase
        self.damage = damage
        self.price = price

    def getDamageoptions(self, dmg):
        self.Damage = dmg
        

    def getPosition(self):
        return self.CurrentTileNode.Value.Position



 
