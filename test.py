# Initialize a 5x5 empty list with '.' as initial values
grid = [["~" for _ in range(5)] for _ in range(5)]

# Function to display the grid with coordinates
def display_grid():
    # Print column coordinates
    print("____ SEA ____")
    print(" ", end=" ")
    for col in range(5):
        print(col, end=" ")

    print()  # Newline after column coordinates

    # Print the grid rows with row coordinates
    for row in range(5):
        print(row, end=" ")  # Print row index
        for col in range(5):
            print(grid[row][col], end="~")  # Print grid value
        print()  # Newline after each row

# Main loop for user input
print("Enter the coordinates and value to fill the grid (e.g., 0 0 A). Type 'exit' to stop.")
while True:
    display_grid()
    user_input = input("Enter coordinates (row column) and value: ").strip()

    if user_input.lower() == "exit":
        print("Final Grid:")
        display_grid()
        break

    try:
        row, col, value = user_input.split()
        row, col = int(row), int(col)

        if 0 <= row < 5 and 0 <= col < 5 and len(value) == 1:
            grid[row][col] = value
        else:
            print("Invalid input. Make sure row and column are between 0 and 4, and value is a single character.")
    except ValueError:
        print("Invalid format. Use the format 'row column value', e.g., '0 0 A'.")
