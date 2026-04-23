import sys
from project import Ground2GroundMetrics, Height2GroundMetrics
from pyfiglet import Figlet
from tabulate import tabulate
from matplotlib import pyplot as plt

#Global Variables
results = []
X_coordinates = []      #contains Lists of List when multiple Projectiles or (only 1 List when single projectile)
Y_coordinates = []      #contains Lists of List when multiple Projectiles or (only 1 List when single projectile)
projectile_number = 0

def main():
    fig = Figlet()
    fig.setFont(font="doom")
    global results, X_coordinates, Y_coordinates, projectile_number

    while True:
        results = []                    #Reinitializing these global variables to delete previous saved memory as this is a continous loop
        X_coordinates = []              #untill sys.exit() is called
        Y_coordinates = []
        projectile_number = 0

        print(fig.renderText("Projectile Simulator ->"), end="")
        print("1) Run Simulation.       2) Compare Trajectories.        3) Exit.")
        match input("\nSelect an option: "):
            case "1": sub_main1()
            case "2": compare()
            case "3": sys.exit(f"{"*"*66}Program Terminated{"*"*66}")
            case _: print("INVALID INPUT!")


def sub_main1():
    print(f"{"-"*67}Simulation Types{"-"*67}")
    print(f"1) Ground to Ground. {" "*75} 2)Height to Ground.")
    menu = input("\nSelect an Option: ")

    match menu:
        case "1": ground_2_ground()
        case "2": height_2_ground()
        case _: print("INVALID INPUT!"), sub_main1()


def sub_main2():
    menu = input(f"""\n{"="*70}WHAT NEXT?{"="*70}
1. Plot graph and Save Results          2. Save results         3. Return to main menu\n
Select an option: """)
    match menu:
        case "1": plot()
        case "2": save()
        case "3": main()
        case _: print("INVALID INPUT!"), sub_main2()


def ground_2_ground():
    print(f"\n{"-"*68}Run Simulation{"-"*68}\n")

    #Error Checking
    while True:
        try:
            # instantiating a projectile object of class Ground2GroundMetrics
            projectile = Ground2GroundMetrics(float(input("Velocity (m/s): ")), float(input("Degree of Projection: ")))
        except ValueError:
            print("INVALID INPUT!")
            pass
        else:
            break

    #Method calls
    projectile.get_coordinates()
    global X_coordinates, Y_coordinates, results
    X_coordinates = projectile.x_coordinates           #Storing all X coordinates in memory to write to .csv or .txt file later.
    X_coordinates.append(projectile.get_range())       #Since the last 'x' value was not exactly equal to range but tends to it.
    Y_coordinates = projectile.y_coordinates           #Storing all Y coordinates in memory to write to .csv or .txt file later.
    Y_coordinates.append(0.0)                          #Since the while true loop in class Projectile y doesn't quite reach 0 but tends to it
    results = projectile.results()                     #Storing Metric data in memory

    print("-"*150)
    print(tabulate([results], tablefmt="fancy_grid"))

    #Function Call to more options
    sub_main2()


def height_2_ground():
    print(f"\n{"-" * 68}Run Simulation{"-" * 68}\n")

    #Error Checking
    while True:
        try:
            projectile = Height2GroundMetrics(float(input("Velocity (m/s): ")), float(input("Degree of Projection: ")),
                                          float(input("Height (m): ")))
        except ValueError:
            print("INVALID INPUT!")
            pass
        else:
            projectile.get_coordinates()
            break

    global X_coordinates, Y_coordinates, results

    X_coordinates = projectile.x_coordinates            #Storing all X coordinates in memory to write to .csv or .txt file later.
    X_coordinates.append(projectile.get_range())
    Y_coordinates = projectile.y_coordinates            #Storing all Y coordinates in memory to write to .csv or .txt file later.
    Y_coordinates.append(0.0)
    results = projectile.results()                      #Storing Metric data in memory

    print(tabulate([results], tablefmt="fancy_grid"))

    sub_main2()


def compare():
    print(f"\n{"-" * 68}Compare Simulation{"-" * 68}\n")

    global projectile_number
    projectile_number = int(input("Enter Number of Projectiles: "))
    values = []
    for num in range(projectile_number):   #Creating List of Dictionaries of velocity:angle pairs for different projectiles user entered

        #Error Checking
        while True:
            try:
                values.append({"velocity": float(input(f"{num + 1}. Velocity (m/s): ")) ,
                               "angle": float(input(f"{num + 1}. Degree Of Projection: "))})
            except ValueError:
                print("INVALID INPUT!")
                pass
            else:
                break

    for pair in values:
        projectile = Ground2GroundMetrics(pair["velocity"], pair["angle"])      #on each iteration instantiating an object or class Ground2GroundMetrics
        projectile.get_coordinates()                                            #and calling required method of that class
        X_coordinates.append(projectile.x_coordinates)
        Y_coordinates.append(projectile.y_coordinates)

        print("-" * 150)
        print(tabulate([projectile.results()],tablefmt="fancy_grid"))

        for metric in projectile.results():
            results.append(metric)

    sub_main2()


def plot():
    print(f"\n{"=" * 70}PLOTTING{"=" * 70}")
    plt.style.use("fivethirtyeight")
    plt.figure(figsize=(11,7))

    if projectile_number != 0:     #indicates more than 1 projectile
        for value in range(projectile_number):
            plt.plot(X_coordinates[value], Y_coordinates[value], label= f"Projectile {value+1}, ")
    else:
        plt.plot(X_coordinates, Y_coordinates, label="Projectile 1")

    plt.legend()
    plt.title("Graph Of Projectile Motion")
    plt.xlabel("Distance (meters)")
    plt.ylabel("Height (meters)")
    plt.grid(True)
    plt.savefig("Plot.PNG")         #save it to current Directory
    plt.show()

    save()


def save():
    print(f"\n{"=" * 71}SAVING{"=" * 71}\n")

    file_name = input("Enter name of file to save as .csv or .txt: ")
    with open(file_name, "w", newline='') as file:
        for metric in results:
            file.write(f"{metric} \n")

    try:
        _ = input(f"{"-"*53}PRESS 'ENTER' TO RESTART OR 'CTRL-D' TO EXIT{"-"*53}\n")
    except KeyboardInterrupt:
        sys.exit(f"{"*"*66}Program Terminated{"*"*66}")
    else:
        pass

if __name__ == "__main__":
    main()