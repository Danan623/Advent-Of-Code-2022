class AdventOfCode:

    def __init__(self):
        # Initialize class members
        self.name = "Daniel Andersson"

    def introduction(self):
        # Access the name of the current instance of the class
        print(
            f"Hello from {self.name}!" + "\n" + "Student in Information Technology at Linköpings University" + "\n" + "My idea is to write every day in the same class (class AdventOfCode)."
            + "\n" + "Each day's code will then be able to run through an instance variable created in the DriverClass." + "\n" * 5)

    # ---------------------------------- advent of code 2022 day 1 task 1 ------------------------------------------
    def day1_task1(self, s: str) -> int:

        # store current item
        current = 0

        # init biggest
        biggest = 0

        # iterate over the list of strings
        for i in s:
            # check if the string is empty then it is a new item
            if i == '':
                # init biggest
                if biggest == 0:
                    biggest = current
                # find the biggest value
                biggest = max(current, biggest)
                # clear item
                current = 0
            # convert from string to int and add the value together
            if i != '':
                current += int(i)

        # convert biggest to a list containing a single element
        biggest = [biggest]
        # return the sum of the biggest value (sum() doesn't work with integer, need a list as argument)
        return sum(biggest)

    # ---------------------------------- advent of code 2022 day 1 task 2 ------------------------------------------
    def day1_task2(self, s: str) -> int:
        # store current item
        current = 0
        # we will need to put the sums in a list or a dict, a list is simpler in this task
        sumList = []

        for i in s:

            # check for new item
            if i != '':
                # convert string and add together
                current += int(i)
            else:
                # put in a list or similar, maybe a dict?
                sumList.append(current)
                # clear current value
                current = 0
        # Sort the list (the highest to the lowest)
        sumList.sort(reverse=True)
        # check the list order
        # print(sumList)

        # add the sums together of the three highest values
        return sumList[0] + sumList[1] + sumList[2]

    # ---------------------------------- advent of code 2022 day 2 task 1 -------***FAIL CODE***------------------------
    # this code will give the wrong output. I can't figure out why, but I think I will need to write in another way
    # read from text file
    def total_score(self, s: str) -> int:
        # stores result
        result = []
        # to test if it will be something with the list, but I don't think so
        test = 0
        # map the values of each combat sign
        yourvalues = {'X': 1, 'Y': 2, 'Z': 3}
        opponentvalues = {'A': 1, 'B': 2, 'C': 3}

        # win and draw scores
        WIN_SCORE = 6
        DRAW_SCORE = 3


        # init score variables for the rounds
        your_round = 0
        opponents_round = 0

        # set counter to check each round
        counter = 0

        for i in s:
            #print(i)
            # Check for space characters and newLine -> ignore
            if i == ' ' or i == '\n':
                continue
            # will give you one string at a time after this

            # look up value of input
            if i in yourvalues:
                your_round = yourvalues[i]

            elif i in opponentvalues:
                 opponents_round = opponentvalues[i]

            # Increment counter
            counter += 1
            print(i)
            # Check if both players have played a "combat sign" in the round
            if counter == 2:
                #print("motsåndare ", opponents_round)
                #print("DU ", your_round)
                # Check the winner of the round
                if your_round > opponents_round:
                    # you win the round = yourRound + 6 points
                    result.append(your_round + WIN_SCORE)
                    #test += your_round + WIN_SCORE
                    #print("vinner")
                elif your_round == opponents_round:
                    # it's a draw = yourRound + 3 points
                    result.append(your_round + DRAW_SCORE)
                    #test += your_round + DRAW_SCORE
                   # print("draw")
                elif your_round < opponents_round:
                    result.append(your_round)
                    #test += your_round
                    #print("förlust")

                # Clear the score variables and start a new round
                your_round = 0
                opponents_round = 0
                counter = 0
                #print("resultat ", test)



        # Return the sum of the result
        return sum(result)

    # ---------------------------------- advent of code 2022 day 2 task 1 ---------------------------------------------
    # take input in a list of strings instead of one character at a time like ["A Z",...]
    # make a table (a dict) with the scores and let the different combinations be key and the integer scores be values
    # mapped to the different keys
    # iterate and check each key - value pair and, store the correct match and return the result
    def day2_task1(self, s: str) -> int:

        table = {"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9,"C X":7, "C Y":2, "C Z":6}
       # table = {"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9,"C X":2, "C Y":6, "C Z":7}
        total = 0
        for i in s:
            #print(i)
            total += table[i]

        return total

    # ---------------------------------- advent of code 2022 day 2 task 2 ---------------------------------------------
    # just change the values in the table.. simple as that
    def day2_task2(self, s: str) -> int:

       # table = {"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9,"C X":7, "C Y":2, "C Z":6}
        table = {"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9,"C X":2, "C Y":6, "C Z":7}
        total = 0
        for i in s:
            #print(i)
            total += table[i]

        return total

    # ---------------------------------- advent of code 2022 day 3 task 1 ---------------------------------------------
    def day3_task1(self, s: str) -> int:
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

    # ---------------------------------- advent of code 2022 day 3 task 2 ---------------------------------------------

    def day3_task2(self, s: str) -> int:
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



