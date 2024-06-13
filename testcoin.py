import random 
 
class Board: 
    def __init__(self): 
        self.snakes = {23:4, 44:2,90:70, 95:65} 
        self.ladder = {5:20, 20:80, 50:96} 
        self.players = {0:1, 1:1, 2:1} 
        self.current_player = 0 
        self.result = [] 
 
     
    # def insert_snakes(self): 
    #     n = int(input()) 
    #     while(n>0): 
     #        n = n-1 
    #         head, tail = map(int,input().split()) 
    #         if not self.ladder.get(tail): 
    #             self.snakes[head] = tail 
     
    # def insert_ladder(self): 
    #     n = int(input()) 
    #     while(n>0): 
          #    n = n-1 
    #         start, end = map(int,input().split()) 
    #         if not self.snakes.get(start): 
    #             self.ladder[start] = end 
 
    #  def insert_player(self): 
    #     n = int(input()) 
    #     for i in range(0,n): 
    #         self.player[i] = 1 
 
 
    def spin(self): 
        return random.randint(1,6) 
     
    def next_player(self): 
        self.current_player = (self.current_player + 1)
        if (self.current_player==len(self.players)):
            self.current_player = 0
        if self.current_player in self.result: 
            return self.next_player() 
        return self.current_player
         
    def get_result(self): 
        i = 1 
        for player in self.result: 
            print("player ", player, "got ", i, "th position")  
            i= i+1 
 
    def game(self): 
        no_of_player = len(self.players) 
        while(len(self.result)<(no_of_player-1)): 
            score = self.spin() 
            print("player", self.current_player, "dice:", score) 
            temp_position = self.players.get(self.current_player) + score 
 
            if temp_position>100: 
                self.current_player = self.next_player() 
            elif temp_position==100: 
                print(self.current_player, "reached target")
                self.result.append(self.current_player) 
            else: 
                self.players[self.current_player] = temp_position
                if self.ladder.get(temp_position): 
                    self.players[self.current_player] = self.ladder.get(temp_position) 
                if self.snakes.get(temp_position): 
                    self.players[self.current_player] = self.snakes.get(temp_position)
                    
            print("player", self.current_player, "current_position:", self.players.get(self.current_player))
             
            self.current_player = self.next_player()
         
        self.result.append(self.current_player) 
        self.get_result() 
     
board = Board() 
board.game()