def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1+num2;
        case "substract":
            return num1-num2;
        case "multiply":
            return num1*num2;
        case "divide":
            if num2 == 0:
                return "Enter a non-zero number."
            elif num2 != 0:
                return num1/num2;
        case _:
            return "Check and enter valid input"

    