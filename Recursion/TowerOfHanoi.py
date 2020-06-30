def move(discs,initial,intermediate,destination):
    if discs == 1:
        print("Move disc ",discs," from ",initial," to ",destination)
        return
    move(discs-1,initial,destination,intermediate)
    print("Move disc ",discs," from ",initial," to ",destination)
    move(discs-1,intermediate,initial,destination)



if __name__ == "__main__":
    move(3,'A','B','C')