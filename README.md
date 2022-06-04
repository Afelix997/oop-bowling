# Bowling Challenge

In this exercise you will write a program to simulate a game of bowling. When you're done you should be able to run an instance of your `Game` class and have it return an array of bowling scores, and a final total score, for a game of bowling.

 Just in case it's been a while since you've last bowled, here is how you keep score:

1. A game has 10 frames(rounds)
2. For each frame a player has two chances to knock 10 pins down.
3. The score for the frame is the total number of pins knocked down.
4. A spare is when the player knocks down all 10 pins in *two* tries.
  * A player will receive a bonus for that frame plus however many pins they knock down in the next roll.
    ~EX: If the score is 10 (total num knocked down) plus a bonus of 5 (num of pins knocked down in the next roll) then the score for the previous frame would be 15.
5. A strike is when a player knocks down all 10 pins in the first try.
  * The bonus in this situation is the value of the next two balls rolled
6. In the 10th frame a player who rolls a spare or a strike is allowed to roll the extra balls.
  * There is a hard cap at three balls in the 10th frame though.

Before starting make sure you understand the nuances of the game studying this example of a game. Walk through each frame making sure the score makes sense as you understand the rolls.

![bowling game frame](http://slocums.homestead.com/files/scrsheet.gif "bowling game frame")
## Purpose


## Release 0 - Create A Frame Class 
The Frame class will be in charge of holding the score for a single frame for a single player. So after our program runs, each player object will have ten frame objects. The frame should know if it is a spare or strike. What instance variables will you need to keep track of for each frame? What methods will you need to create? 
 
## Release 1 - Create a Player Class 
The player class will keep track of the player's score through out the game. The player should hold frame objects. It should be able to iterate over the frames and calculate the current score. 

## Release 2 - Create the Game Class 
The game class will be in charge of game logic. It should hold players, know what frame is currently being bowled and how many frames are left in the game. This is where you'll write your logic to simulate the game. What method or methods will you need to 'bowl' a frame? Your game class should have a method `play` that simulates a game and returns the scores for each player. 


