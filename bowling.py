import random

class Game:    
    def __init__(self, player_name):
        self.player_name=player_name
        self.score_list= []
        self.final_score=0
        self.frame=0
        self.rem_frames=10

   

    def roll(self):
        for i in self.players:
            i.player_roll()
        self.frame+=1
        self.rem_frames-=self.frame
    
    def current_scores
        
        

    def play(self):
        pass
    def __str__(self):
        return f'All Scores:{self.score_list}/nFinal Score: {self.final_score}'


class Frame():
    def __init__(self,frame_number,player_name):
        self.player_name=player_name
        self.current_frame=frame_number
        self.frame_score=0

    def roll(self):
        first_roll= random.randint(0,10)
        if first_roll == 10:
            self.frame_score=10
            return [f"{self.current_frame}", 'strike', 10] 
        rem_pins=10-first_roll
        second_roll=random.randint(0,rem_pins)
        if first_roll + second_roll == 10:
            self.second_roll=0
            self.frame_score=10
            return [f"{self.current_frame}", , 10]
        self.frame_score= first_roll + second_roll
        return [first_roll, second_roll]
    

class Player(Frame):
    
    def __init__(self,name):
        self.frame_strike=False
        self.strike_counter=0
        self.frame_spare=False
        self.spare_counter=0
        self.current_player=name
        self.frame=0
        self.player_current_score
        self.all_frames=[]


    def player_roll(self):
        self.frame +=1
        frame=self.frame
        frame = Frame(self.frame,self.current_player)
        result= frame.roll()
        if result[0] == "strike" and self.strike_bonus == False:
            self.strike_bonus=True
            self.all_frames.append([f"Frame {self.frame}", 10 ]) 
        elif result[0] == "strike" and self.strike_bonus == True:

        elif result == "spare":
            self.frame_spare=True
            self.spare_counter=1
        else: 
            self.player_current_score= frame.roll()
        
        


         
        
        
    

        
    





