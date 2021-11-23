# Tic Tac Toe
I have decided to recreate the iconic childhood game of tic-tac-toe into a Python terminal game, which will run on Heroku.
Users can try to beat the computer by trying to place 3 of their markers in a row, the board will be shown before any moves are made and after each players makes a move.

## Flow Chart
![Flow Chart](documentation/ttt-flowchart.png)

## How To Play
My Python terminal version of tic-tac-toe is based on the childhood pen and paper game. You can read more about it on the [Tic Tac Toe Wiki](https://en.wikipedia.org/wiki/Tic-tac-toe)

The game follows the generic rules or the paper based version.
* The board is drawn out.
* Who goes first is decided.
* The first player makes their move and the board will be shown with their move in place.
* Then the second player will make their move and the board will be shown again.
* Keep alternating moves until one of the players has drawn a row of 3 or until no one can win.

Those are the basic steps of how a single game of tic-tac-toe works.

## Features

### Main Menu
* The main menu feature will consist of 4 options for the user to choose from: 
    * Play Game - starts the game.
    * How to play - explains how the game works.
    * About - explains what tic-tac-toe is.
    * Exit - exits the game.

* The reason for the main menu is to make the project more visually appealing and to allow the user to understand what is happening rather than being thrown directly into the game expected to know what tic-tac-toe is and how to play it.


### Board Generation
* The first feature of this project is visually one of the most important aspects, the board, this feature allows the user to see all possible moves they can make without having to keep a mental note of previous moves made by themselves or the computer.
* screenshot here

### User Input
* User input is what allows the user/player to input their moves, the players input is limited to only numbers between 0-8 as those are the only available moves on the board.
* With each turn that goes by the user will have less options meaning their input options are also less, any input not valid will throw an error message and ask them to try again.

### Board Updates
* Similar to the board generation this feature allows the board to update after each and every move allowing the user to see an updated version of the board so it's even easier to see the next moves.

### Computer Player
* This feature allows the user to play against a computer player who randomly generates the moves it makes.

### Check Win
* The check win feature is an important feature that is run after every move to check and recheck if anyone has won, it does this by checking all horizontal, vertical and diagonal winning combonations and returns the results.

### Check Tie
* The check tie feature is similar to the check win except instead of checking for 3 of the same in a row it simply returns a tie if the check win feature does not return as true.


### Future Features
* Random player goes first?
* Play again
* Invalid option
* Invalid input
* Game over
* Menu screen