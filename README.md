
# Turtle Race Game

This is a simple Python game using the Turtle graphics module, where users can place a bet on which turtle will win a race. The turtles race across the screen, and the game announces the winner based on the user's bet.

## Features

- **Race Setup**: The race track, consisting of start and finish lines, is drawn automatically.
- **Turtles**: Six turtles, each with a unique color, race from the start to the finish line.
- **Betting System**: The player can bet on one of the turtles by choosing a color.
- **Race Outcome**: Once a turtle crosses the finish line, the winner is announced, and the player is notified whether their bet was correct.

## Requirements

- Python 3.x
- `turtle` module (typically included in standard Python distributions)

## How to Run

1. **Clone the Repository**: Use Git to clone the repository to your local machine. Run the following command:

    ```bash
    git clone https://github.com/12Rajnitish/turtle-race.git
    ```    

2. **Navigate to the Project Directory**: After cloning the repository, move into the project folder:

    ```bash
    cd turtle-race 
    ```

3. **Run the Script**: Once inside the project folder, run the script with the following command: 

    ```bash
    python turtle_race.py
    ```

4. When prompted, enter the color of the turtle you believe will win the race.
5. Watch the turtles race across the screen and see if your chosen turtle wins!

## Code Overview

### 1. `goto_start_pos(turtle_list)`
This function sets the starting positions for all turtles in the race.

### 2. `race_setup()`
Draws the race track and displays the welcome message at the top of the screen.

### 3. `winner_notice(msg)`
Displays the message announcing the winner at the bottom of the screen.

### 4. `Main Game Loop`
- Initializes the race and prompts the user to make a bet on the turtle color.
- Each turtle moves randomly until one crosses the finish line.
- Once the race ends, the winner is announced, and the player's result is displayed.

## Example of Output

1. A prompt will ask you to choose a turtle color.
2. The turtles will race across the screen, and the result will be displayed in the console and visually on the screen.

Example console output:

```
You've Won! Red turtle wins!
```

## License

This project is open-source and free to use under the MIT License.
