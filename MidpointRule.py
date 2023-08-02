def midpoint(formula, upperbound, lowerbound, numberOfRectangles):
    formula = formula.replace("^", "**")
    width = (upperbound - lowerbound) / numberOfRectangles
    print ("width: ", width)
    area = 0
    print ("midpoint: ", end="")
    for i in range (numberOfRectangles):
        print ("(", lowerbound + width * (i + 0.5),")", end=" ")
    for i in range(numberOfRectangles):
        area += width * eval(formula, {"x": lowerbound + width * (i + 0.5)})
    print("")
    return area

formula = input("Enter the function: ")
upperbound = int(input("Enter the upper bound: "))
lowerbound = int(input("Enter the lower bound: "))
numberOfRectangles = int(input("Enter the number of rectangles: "))
print("Area:", midpoint(formula, upperbound, lowerbound, numberOfRectangles))
input("Press enter to exit")