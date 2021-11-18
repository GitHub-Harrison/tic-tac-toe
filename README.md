# Tic Tac Toe
I have decided to recreate the iconic childhood game of tic-tac-toe into a Python terminal game, which will run on Heroku.
Users can try to beat the computer by trying to place 3 of their markers in a row, the board will be shown before any moves are made and after each players makes a move.

## How To Play
My Python terminal version of tic-tac-toe is based on the childhood pen and paper game. You can read more about it on __Add link to wiki page.

The game follows the generic rules or the paper based version.
* The board is drawn out.
* Who goes first is decided.
* The first player makes their move and the board will be shown with their move in place.
* Then the second player will make their move and the board will be shown again.
* Keep alternating moves until one of the players has drawn a row of 3 or until no one can win.

Those are the basic steps of how a single game of tic-tac-toe works.

## Features
### Future Features
* Board generation
* User input
* Board updates
* Random player goes first?
* Play again
* Invalid option
* Invalid input
* Game over


## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!