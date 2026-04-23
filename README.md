Video Demo: https://youtu.be/ZuT9uNq98R8?si=GCl7PrXWYrBSxDgj
Description: # 📌 Projectile Motion Simulator – Description
This project is a command-line based projectile motion simulator designed to model and analyze the trajectory of objects under the influence of gravity. Using the Newton's Laws of Motion to determine the position of the projectile in (x,y) with respect to time, the program calculates important data and stores it in various forms. The program also allows users to input initial conditions such as velocity and angle of projection, and based on the selected type of motion—either ground-to-ground or height-to-ground it computes and visualizes the resulting trajectory.

The simulator is built around a continuous interactive loop, enabling users to perform multiple simulations in a single session without restarting the program. This design emphasizes usability rather than a simple one-time script execution. Users can experiment with different inputs efficiently and observe how changes in parameters affect the motion.

A key feature of the program is its ability to compare multiple trajectories simultaneously. Users can input multiple sets of parameters, and the simulator plots all resulting trajectories on a single graph, making it easier to analyze differences in range, height, and overall motion. There is no fixed limit on the number of trajectories that can be compared, allowing for flexible experimentation.

The program also includes functionality for exporting results. Users can choose to save simulation data to .txt or .csv files, as well as save graphical plots for further analysis or reporting. Alternatively, users can opt to save only the data (as .txt or .csv) without generating a graph, providing flexibility based on their needs.

Overall, this project combines physics-based modeling with structured programming and user interaction to create a useful tool

🚀 Projectile Motion Simulator – Features
1. Multiple Projection Types
Supports ground-to-ground projections
Supports height-to-ground projections
Automatically handles calculations based on initial conditions
2. Interactive CLI Interface
Runs in a continuous loop within the command line
Users can perform multiple simulations without restarting the program
Designed as a modular system, not a single top-to-bottom script
3. Multi-Trajectory Comparison
Users can compare multiple ground-to-ground projections
All trajectories are plotted on a single graph for visual comparison
4. Scalable Simulation Input
No fixed limit on comparisons
Users can simulate as many trajectories as desired in one session
5. Data & Graph Export Options
Option to save simulation data as:
.txt file
.csv file
Option to save the graph output of simulations
6. Flexible Saving Control
Users can choose to:
Save both data and graph
Save only simulation data
Skip saving entirely
7. Computed Simulation Metrics
Based on user input (initial velocity and angle of projection), the simulator automatically calculates:
Time of Flight
Maximum Height
Range of Projectile
Calculations adapt depending on the type of projection (ground-to-ground or height-to-ground)
8. Structured Output Display
Simulation results are displayed in the command line in a clean, tabular format
Ensures outputs are:
Easy to read
Well-organized
Comparable across multiple simulations
🧩 Program Structue & Design
The project is divided into two main files: main_project.py and project.py to ensure separation of concerns and better code organization. The project follows an object-oriented design to organize the simulation logic and improve code modularity and reusability. At its core, the file project.py defines three classes and main_project.py defines 8 functions and 4 global variables:

📁 project.py (Core Logic)
Contains all the core computational logic of the simulator
Defines the class hierarchy:
Projectile (base class)
Ground2GroundMetrics (subclass) - Inherits from Projectile all instance variables and 1 instance method get_coordinates(self)
Height2GroundMetrics (subclass) - Inherits from Projectile all instance variables
Responsible for:
Performing physics calculations
Generating trajectory data (coordinates)
Computing key metrics (time of flight, range, maximum height)
Projectile class calculates each x_coordinate and y_coordinate at 0.05 seconds interval to get the projectile coordinates according to user inputs this is done in get_coordinates method of that class
📁 main_project.py (Command-Line Interface)
Acts as the interactive layer of the program
Handles:
User input
Menu navigation
Data presentation
Runs in a continuous loop, allowing the program to execute indefinitely until the user chooses to exit
🔧 Functional Breakdown
The CLI is structured into multiple functions:

main

Entry point of the program
Displays the main menu
Allows user to choose between:
Running simulations
Comparing trajectories
exit program
sub_main1

Handles simulation mode (non-comparison)
Prompts user to select the type of projection:
Ground-to-ground
Height-to-ground
sub_main2

Executed after any type simulation is completed
Provides options to:
Save data and plots
Save only data
Return to the main menu
ground_2_ground / height_2_ground

Responsible for:
prompting user for velocity and angle and/or height
Creating instances of respective classes Ground2GroundMetrics / Height2GroundMetrics
Calling class methods of required classes
Displaying formatted results
compare

prompts the user for number of prjectiles
Handles multiple user inputs of velocity and angle of each projectile
Runs and stores multiple simulations
Displays results in a structured format
save and plot

Triggered based on user choice
Handle exporting of data and visualization
🛡️ Input Validation & Error Handling
The program incorporates error handling to ensure reliable user interaction and prevent invalid simulations.

✔ Input Validation
Ensures that velocity and angle of projection are valid numeric inputs (int or float)
Prevents execution with invalid or malformed data
Automatically re-prompts the user until valid input is provided
🔁 Menu-Level Validation
All menu functions (main, sub_main1, sub_main2) include validation checks
If the user enters an invalid option which is not displayed in that sepecific menu:
The program does not crash
The user is re-prompted to enter a valid choice
🎯 Result
Improves overall user experience
Makes the simulator fault-tolerant
Ensures consistent and predictable behavior during extended use
📊 Data Management
The program uses several global variables to persist data across functions:

results → stores computed metrics
X_coordinates, Y_coordinates → store trajectory data
projectile_number → tracks number of simulations
This approach allows different parts of the program to access shared data without requiring complex return chains between functions.

🧠 Design Justification
This structure was chosen for practical reasons:

Separation of logic and interface

project.py focuses purely on computation
main_project.py focuses on interaction
Improved readability

Avoids overcrowding a single file with all logic
Reduced error surface

Changes in simulation logic do not affect CLI handling and vice versa
Easier to debug and maintain
Scalability

Additional features (e.g., new simulation types) can be added easily
