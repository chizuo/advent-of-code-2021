from constants import banner, interface, onSelect, onQuestion


def main():
    cache = {}
    option = -1
    [print(line) for line in banner]
    while(option != 0):
        option = interface()
        if(option != 0):
            onQuestion(
                input("\nWould you like to read the problem? [Y]es or [N]o: "), option)
            if(option in cache):
                day = cache.get(option)
            else:
                day = onSelect(option)
                cache[option] = day
            day.solution()
            input("\n\nPress any key to continue...\n")
        else:
            print("\n*** Thank you for demoing my Advent of Code 2021 ***\n")


main()
