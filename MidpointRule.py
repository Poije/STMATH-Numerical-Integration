def midpoint(formula, upperbound, lowerbound, numberOfRectangles):
    width = (upperbound - lowerbound) / numberOfRectangles
    area = 0
    for i in range(numberOfRectangles):
        area += width * eval(formula, {"x": lowerbound + width * (i + 0.5)})
    return area

formula = input("Enter the function: ")
upperbound = int(input("Enter the upper bound: "))
lowerbound = int(input("Enter the lower bound: "))
numberOfRectangles = int(input("Enter the number of rectangles: "))
print(midpoint(formula, upperbound, lowerbound, numberOfRectangles))