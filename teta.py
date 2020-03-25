'''
Moje teta - tvoje teta
pravidla:   32 karet (7,8,9,10,J,Q,K,A)
            zamíchám
            ukazuji poslední kartu z balíku
            hráč si vybere dvě pole, na jedno vsadí, na druhé ne
            padne-li typ (neřeším barvu, ale vizuálně jo), vyhrává za každou co tam padne
        
'''

def End(positions):
     for i in range (8):
          le = len(positions.positions[i])
          if le > 4:
               player = positions.positions[i][0][0]
               value = positions.positions[i][0][1]
               amount = positions.positions[i][0][2]
               for z in range (1,le):
                    if positions.positions[i][z].numb == str(value):
                         print(f"{player} wins {amount}")

def Play(positions,deck):
     p = 0
     for i in range (32):
          positions.play(p,deck.cards[0])
          deck.remove()
          p = p+1
          if p == 8:
               p = 0
     End(positions)
     
class Positions:
     
     def __init__(self):
          
          self.positions = []
          for i in range(0,8):
               self.positions.append([])
          
     def bet(self, p1,v1,amount,p2):
          
          self.positions[p1].append(["Player",v1,amount])
          self.positions[p2].append(["Dealer",v1,amount])
          
     def play(self,p,card):
          
          self.positions[p].append(card)
    
class Card:
    
     def __init__(self,numb,color):
          
         self.numb = numb
         self.color = color
         
class Deck:

     def shuffle(self):
          
        import random
        random.shuffle(self.cards)
        
     def last(self):
          
          return self.cards[-1]
    
     def __init__(self):
          
          self.cards = []
          cards = ["7","8","9","10","J","Q","K","A"]
          for card in cards:
               self.cards.append(Card(card,0))
               self.cards.append(Card(card,1))
               self.cards.append(Card(card,2))
               self.cards.append(Card(card,3))

     
     
     def remove(self):
          self.cards = self.cards[1:]       
          
        
if __name__ == '__main__':
     deck = Deck()
     deck.shuffle()
     deck.shuffle()
     deck.shuffle()
     positions = Positions()
     print(deck.last().numb,deck.last().color)
     print("if you want to bet, type positions.bet(your position, value you are betting on, ammount of money and then dealers position")
     print("After bets, type Play(positions,deck)")
