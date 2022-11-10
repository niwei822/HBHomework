def melon_report(day_number, path):
    """ Use day number and file path as parameter to read line by line, split each line by |
    then give index to print report """
    print("Day", day_number)

    for line in open(path):
        line = line.rstrip()
        words = line.split('|')
    
        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    open(path).close()
melon_report(1, "um-deliveries-day-1.txt")
melon_report(2, "um-deliveries-day-2.txt")
melon_report(3, "um-deliveries-day-3.txt")
