
# ---------------------------- Functions ------------------------------- #

def extended_euclid_algorithm(a: int, b: int) -> tuple:

    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
   
    x = 0
    y = 1
    x_prev, y_prev = 1, 0
    
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x, x_prev = x_prev - quotient * x, x
        y, y_prev = y_prev - quotient * y, y
        
    return (a, x_prev, y_prev)


# ---------------------------- Variables ------------------------------- #

first_num = None
second_num = None


# ------------------------------ Main ---------------------------------- #

if __name__ == "__main__":

    # get valid numbers
    while first_num is None or second_num is None:

        print()
        input_a = input("Enter the first number: ")
        input_b = input("Enter the second number: ")
    
        # check for valid input
        if input_a.isdigit() and input_b.isdigit():
            first_num = int(input_a)
            second_num = int(input_b)

        else:
            print()
            print("Invalid Input!\nPlease enter two numbers.")

    # sort the numbers
    if second_num > first_num:
        first_num, second_num = second_num, first_num 

    try:
        result = extended_euclid_algorithm(first_num, second_num)
    except ValueError as e:
        print()
        print(f"Error: {e}")
        exit(1)

    # Return the results
    print()
    print("Result:")
    print("-" * 11)
    print(f"GCD: {result[0]}")
    print(f"{first_num}⁻¹: {result[1]}")
    print(f"{second_num}⁻¹: {result[2]}")

