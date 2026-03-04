dimentions = input("Provide dimentions to calculate: ").split()
if dimentions == 2:
    width, height = dimentions
    try:
        width = int(width )
        print()

    except:
        ValueError 

else:
    print("provide 2 digits")