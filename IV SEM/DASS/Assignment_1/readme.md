# Assignment 1


## Question 1: Marks Manager 

### Usage

1. **Adding Entry:**
   - Choose option `1` from the menu.
   - Enter student details (First Name, Last Name, Roll Number).
   - Provide semester, course name, exam type, total marks, and scored marks.
   - Every entry must be unique.

2. **Displaying Table:**
   - Choose option `2` from the menu to display a tabular view of the entered data using prettytable.

3. **Removing Entry:**
   - Choose option `3` from the menu.
   - Enter student details, semester, course name, and exam type to remove the entry.
   - As all the rows are unique so u have to enter all details.
   - Only one Entry can be removed at a time

4. **Updating Entry:**
   - Choose option `4` from the menu.
   - Enter student details, semester, course name, and exam type to update the total and scored marks.
   - Only Marks can be updated.

5. **Searching Entry:**
   - Choose option `5` from the menu.
   - Enter attributes to search for (e.g., FirstName, Semester, LastName, RollNo, CourseName, ExamType).

6. **Saving to File:**
   - Choose option `6` from the menu to save the entered data to a CSV file.

7. **Quitting:**
   - Choose option `7` from the menu to exit the program. The data will be saved to the CSV file before quitting.


### Command-line Arguments

You can provide a CSV file as a command-line argument to load existing data when running the script. For example:

```bash
python mdirectory.py data.csv
```

If no file is provided, the script will use a default file named `marks.csv`.

### Note

- The script uses the `prettytable` library to display the data in a formatted table.
- If you encounter any issues or have questions, please refer to the code comments or contact the script author.






## Question 2: Map Plotting

This Python script creates a simple 2D vector movement plotter using the Matplotlib library. The script allows users to input distance and direction commands to simulate movement in a 2D space.

### Usage

1. Enter distance and direction commands, separated by a space.
2. Press ENTER after each command.
3. To stop, enter "0 0".
4. The script will display the final destination, relative to the starting point, and a plot of the movement.

### Vector Class

The `vector` class represents a 2D vector and provides methods to add distance and direction, print coordinates, plot movement, and print the final destination relative to the starting point.

#### Class Methods

- `AddDistance(distance, direction)`: Adds the specified distance in the given direction to the vector.
- `printCoord()`: Prints the current coordinates and the entire path traversed.
- `plot_movement()`: Plots the movement path using Matplotlib.
- `printRelative()`: Prints the final destination relative to the starting point.

### Dis Class
- This class handles unit conversions for distances.
- Supported units: "mm", "cm", "m", "km".

### Directional Commands

The following directional commands are supported:

- N: North
- NE: Northeast
- NW: Northwest
- E: East
- W: West
- S: South
- SE: Southeast
- SW: Southwest

### Example

```plaintext
Enter distance and direction ("0 0" to stop):
(press ENTER after every command)

10m nE
5km w
8mm Sw
100cm s
0 0
```


## Question3: Kaooa Board Game

This Python program implements a simple two-player board game with a star pentagram board layout. The game involves two players, "Crow" and "Vulture," and the goal is to either eliminate all crows (Crow wins) or trap the vulture so it cannot make a legal move (Vulture wins).

### How to Play

1. **Crow's Turn:** Click on a crow to select it. Then, click on an empty position (star point) to move the crow to that location. Crows can only move to adjacent empty positions.

2. **Vulture's Turn:** Click on the vulture to select it. Then, click on an empty position to move the vulture to that location. Vulture has additional killing moves, eliminating a crow on an adjacent position.

3. **Winning Conditions:**
   - **Vulture Wins:** Eliminate 4 crows from the board.
   - **Crow Wins:** Trap the vulture so it cannot make a legal move.

4. **Main Menu:**
   - Press "1" to start a new game.
   - Press "2" to exit the game.

### Game Components

#### Board
- The game board is a star pentagram with outer circles and vertices.
- Circles represent the star points and can be occupied by crows or the vulture.

#### Crow
- Crows are represented by blue circles on the board.
- Crows move to adjacent empty positions.

#### Vulture
- The vulture is represented by a red circle on the board.
- The vulture can move to adjacent empty positions and has special killing moves.

#### Place
- Manages the game state, including player turns, crow and vulture positions, and empty positions.
- Tracks the number of crows eliminated (kill count).

#### Game
- Initializes the Pygame window, handles user input, and manages the game loop.
- Provides a main menu for starting a new game or exiting.

