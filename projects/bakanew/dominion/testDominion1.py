# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:09:42 2020

@author: Wes Bakane
"""
import Dominion
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#Calculate number of victory and curse cards
nV = testUtility.NumVictoryCards(len(player_names))
nC = testUtility.NumCurseCards(len(player_names))

#Initialize boxes
box = testUtility.GetBoxes(nV)

supply_order = {0:['Curse','Copper','Province'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

#Initialize supply
supply = testUtility.GetSupply(box, len(player_names))

#The supply always has these cards
supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
supply["Silver"]=[Dominion.Silver()]*40
supply["Gold"]=[Dominion.Gold()]*30
supply["Estate"]=[Dominion.Estate()]*nV
supply["Duchy"]=[Dominion.Duchy()]*nV
supply["Province"]=[Dominion.Province()]*nV
supply["Curse"]=[Dominion.Curse()]*nC

#Initialize the trash
trash = testUtility.GetTrash()

#Initialize players
players = testUtility.GetPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)