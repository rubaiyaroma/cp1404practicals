def main():
    kevin = Drummer("Kevin Figueiredo")
    gary = Guitarist("Gary Cherone")
    nuno = Guitarist("Nuno Bettencourt")
    paula = Singer("Paula Cole")

    band = [kevin, gary, nuno, paula]

    for musician in band:
        print(musician.play())

if __name__ == "__main__":
    main()
