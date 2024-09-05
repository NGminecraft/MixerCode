print("ABC\n123", end="\r")
print("ABC\nZYX")
print(("\033[F"+"\033[2K")*3)