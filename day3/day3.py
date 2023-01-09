with open(r"src\advent_of_code2022\day3\day3.txt", "r") as f: # 14610
    numbers = f.read()

number = numbers.split("\n")

def day3_task1(s: str) -> int:
    # I didn't read the task so well at first so failed my first tries.
    # Create a table with key value pairs. iterate through the items.
    # split the string into two substrings
    # if the second substring contains a character (string) -> found a pair
    table = {
        "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,
        "o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,
        "A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,
        "O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52
    }

    # init total
    total = 0

    # iterate through the items
    for string_seq in s:

        # split the string in two
        tmp_string1 = string_seq[:len(string_seq)//2]
        tmp_string2 = string_seq[len(string_seq)//2:]

        for character in tmp_string1:
            # found a matching pair
            if character in tmp_string2:
                total += table[character]
                break

    return total

def day3_task2(s: str) -> int:
    # creates a table with the key value pair
    table = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
        "n": 14,
        "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
        "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38,
        "M": 39, "N": 40,
        "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52
    }

    # init total and flags
    total = 0
    flag1 = True
    flag2 = False
    flag3 = False

    # iterate through the items
    for string_seq in s:

        # create a group of three string sequence
        if flag1:
            subgroup1 = string_seq
            flag1 = False
            flag2 = True
            flag3 = False
            continue
        elif flag2:
            subgroup2 = string_seq
            flag1 = False
            flag2 = False
            flag3 = True
            continue
        elif flag3:
            subgroup3 = string_seq
            flag1 = True
            flag2 = False
            flag3 = False
        # print(subgroup1)
        # print(subgroup2)
        # print(subgroup3)
        for character in subgroup1:

            if character in subgroup2:

                if character in subgroup3:
                    # print(character)
                    total += table[character]
                    break

    return total

result = day3_task1(number)  # *********** correct ****************
print("advent of code 2022 day 3 task 1: ", result)

result = day3_task2(number)  # *********** correct ****************
print("advent of code 2022 day 3 task 2: ", result)