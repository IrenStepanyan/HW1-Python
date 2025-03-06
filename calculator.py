def calculator():
    print("Enter your calculation. (enter 'exit' for stopping the program")
    while True:
        try:
            exp = input("Enter your calculation: ")
            if exp.lower() == 'exit':
                print("Exit")
                break
            result = eval(exp)
            print(result)
        except:
            print("Invalid error! Please try again.")
calculator()
