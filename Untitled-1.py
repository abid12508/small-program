#some random program i made.
points = 0
print("get all of the questions right")
print("1+1")
if input() == str(2):
    print("correct")
    points += 1
    print(points)
elif input() != str(2):
    points -= 1
    print(points)
print("2+2")
if input() == str(4):
    print("correct")
    points += 1
    print(points)
elif input() != str(4):
    points -= 1
    print(points)
print("3+3")
if input() == str(6):
    print("correct")
    points += 1
    print(points)
elif input() != str(6):
    points -= 1
    print(points)
print("4+4")
if input() == str(8):
    print("correct")
    points += 1
    print(points)
elif input() != str(8):
    points -= 1
    print(points)
print("5+5")
if input() == str(10):
    print("correct")
    points += 1
    print(str(points) + "/5")
elif input() != str(10):
    points -= 1
    print(points)
    print(str(points) + "/5")
    if points == -5:
        print("lol u got negative points")
    elif points == -4:
        print("lol u got negative points")
    elif points == -3:
        print("lol u got negative points")
    elif points == -2:
        print("lol u got negative points")
    elif points == -1:
        print("lol u got negative points")
    elif points == 0:
        ("you got none right lol")
else:
    print(str(points) + "/5")
