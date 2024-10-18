#Calculator by Sarvamm
import math
def draw():
    global userinput, result
    l = len(userinput)
    r = len(str(result))
    
    print(" " + "-"*l + "-"*(16-l))
    print("|", userinput + " "*(15-l) + "|")
    print(" " + "-"*l + "-"*(16-l))
    print(" "*(15-r) + "= " + str(result))
    print("-----------------") 
    # print("|** | / | * |Clr|")
    # print("----+---+---+----")
    # print("| 7 | 8 | 9 | - |")
    # print("----+---+---+----")
    # print("| 4 | 5 | 6 | + |")
    # print("----+---+---+----")
    # print("| 1 | 2 | 3 | = |")
    # print("-----------------")

def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return """Error (division by zero)"""
    except Exception:
        return "Error (invalid input)"

result = "" 
userinput = ""
while True:
    x = input("Input: ")
    
    if x.lower() in ['c', 'clr', 'clear']:
        userinput = ""
        result = ""
        print("cleared.")
    elif x == "=":
        result = calculate(userinput)
    else:
        userinput = str(result) + x
        result = calculate(userinput)
    
    draw()
    if result in ["Error (division by zero)", "Error (invalid input)"] or type(result) == bool:
        userinput = ""
        result = ""
