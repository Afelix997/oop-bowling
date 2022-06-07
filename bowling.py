import random

class Game:    
    def __init__(self, player_name):
        self.player_name=player_name
        self.score_list= []
        self.final_score=0
        self.frame=0
        self.rem_frames=10

   

    def play(self):
        self.player_name = Player(self.player_name)
        while self.frame<11:
            self.player_name.player_roll()
            self.frame+=1
            self.rem_frames-=self.frame
        self.final_score= self.player_name.calc_score()
        self.score_list= self.player_name.res_list()
        return print(self.score_list, self.final_score)
        
    
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
            return [f'Frame {self.current_frame}', 'strike',0, 10]
        rem_pins=10-first_roll
        second_roll=random.randint(0,rem_pins)
        if first_roll + second_roll == 10:
            self.frame_score=10
            return [f'Frame {self.current_frame}',first_roll ,'spare', 10]
        self.frame_score= first_roll + second_roll
        return [f'Frame {self.current_frame}',first_roll,second_roll, self.frame_score]

    def roll_last(self):
        last_first_roll= random.randint(0,10)
        if last_first_roll==10:
            last_second_roll= random.randint(0,10)
            if last_second_roll==10:
                last_third_roll=random.randint(0,10)
                if last_third_roll==10:
                    return [f'Frame {self.current_frame}','strike','strike','strike' , 30]
            rem_pins=10-last_second_roll
            last_third_roll=random.randint(0,rem_pins)
            self.frame_score=last_second_roll+last_third_roll+10
            return [f'Frame {self.current_frame}','strike',last_second_roll,last_third_roll , self.frame_score]
        rem_pins=10-last_first_roll
        last_second_roll=random.randint(0,rem_pins)
        if last_first_roll + last_second_roll == 10:
            last_third_roll=random.randint(0,10)
            self.frame_score=10+last_third_roll
            return [f'Frame {self.current_frame}',last_first_roll,last_second_roll,last_third_roll , self.frame_score]
        self.frame_score=last_first_roll+last_second_roll
        return [f'Frame {self.current_frame}',last_first_roll,last_second_roll, self.frame_score]

class Player(Frame):
    
    def __init__(self,name):
        self.current_player=name
        self.frame=0
        self.all_frames=[]


    def player_roll(self):
        self.frame +=1
        frame=self.frame
        frame = Frame(self.frame,self.current_player)
        if self.frame<10:
            result= frame.roll()
            self.all_frames.append(result)
        if self.frame==10:
            result=frame.roll_last()
            self.all_frames.append(result)
            self.strike_calc()
            print(self.all_frames)
            return print(f'Rolling Frame {self.frame}') 
           
    def strike_calc(self):
        frames_list= self.all_frames
        print(frames_list[9],'YES')
        for i,list in enumerate(frames_list):
            if i<8:
                if list[1]=='strike' and frames_list[i+1][1]== 'strike' and frames_list[i+2][1]=='strike':
                    frames_list[i][3]= list[3]+frames_list[i+1][3]+frames_list[i+2][3]
                elif list[1]=='strike' and frames_list[i+1][1]== 'strike':
                    frames_list[i][3]=list[3]+frames_list[i+1][3]+frames_list[i+2][1]
                elif list[1]=='strike' and frames_list[i+1][2]== 'spare':  
                    frames_list[i][3]=list[3]+ frames_list[i+1][3]
                elif list[1]=='strike':   
                    frames_list[i][3]=list[3]+frames_list[i+1][1]+frames_list[i+1][2]
                elif list[2]=='spare' and frames_list[i+1][1]== 'strike':
                    frames_list[i][3]+= frames_list[i+1][3]   
                elif list[2]=='spare':
                    frames_list[i][3]+=frames_list[i+1][1]
            if i==8:
                if list[1]=='strike':
                    frames_list[i][3]=frames_list[i+1][1]+frames_list[i+1][2]
                elif list[2]=='spare' and frames_list[i+1][1]== 'strike':
                    frames_list[i][3]=frames_list[i][3] + frames_list[i+1][2] + + frames_list[i+1][3] +10
                elif list[2]=='spare':
                    frames_list[i][3]+=frames_list[i+1][1]    
        self.all_frames= frames_list

    def calc_score(self):
        frames_list=self.all_frames
        result=0
        for i,checking in enumerate(frames_list):
            if i < 9:
                result = result+frames_list[i][3]
            if i==10:
                result = result+frames_list[i][4]    
        return result

    def res_list(self):
        return self.all_frames
        
        


         
        
        
    

        
    





