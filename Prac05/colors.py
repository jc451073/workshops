__author__ = 'jc451073'
Color_list={"beige": "#f5f5dc","bisque1": "#ffe4c4","bisque3": "#cdb79e","blue1": "#0000ff","blue2": "#0000ee",}
color=input("enter the color to get code")
while color != " ":
    if color in Color_list:
        print(color,"is",Color_list[color])
    else:
        print("Invalid color")
    color = input("Enter color again: ")