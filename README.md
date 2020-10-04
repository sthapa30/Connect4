# Programming Assignment - Game Playing Algorithms
The task in this programming assignment is to implement an agent that plays the Max-Connect4 game using
search.The game is played on a 6x7 grid, with six rows and
seven columns. There are two players, player A (red) and player B (green). The two players take turns placing
pieces on the board: the red player can only place red pieces, and the green player can only place green pieces.

The game is over when all positions are occupied. Obviously, every complete game consists of 42 moves, and
each player makes 21 moves. The score, at the end of the game is determined as follows: consider each
quadruple of four consecutive positions on board, either in the horizontal, vertical, or each of the two diagonal
directions (from bottom left to top right and from bottom right to top left). The red player gets a point for each
such quadruple where all four positions are occupied by red pieces. Similarly, the green player gets a point for
each such quadruple where all four positions are occupied by green pieces. The player with the most points wins
the game.

![connect4](https://user-images.githubusercontent.com/22757695/95021233-5c822b00-0635-11eb-8313-951a9bae4131.gif)


## How to run the program
python maxconnect4 interactive [input_file] [computer-next/human-next] [depth]

