__author__ = 'jc451073'
Color_list={"beige": "#f5f5dc","bisque1": "#ffe4c4","bisque3": "#cdb79e","blue1": "#0000ff","blue2": "#0000ee",}


print(Color_list['beige'])

color=input("enter the color to get code")

while color != " ":
    if color in Color_list:
        print(Color_list[color])
    else:
        print("Invalid color")
    color = input("Enter color again: ")