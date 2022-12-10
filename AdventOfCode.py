
class AdventOfCode:

    def __init__(self):
        # Initialize class members
        self.name = "Daniel Andersson"

    def introduction(self):
        # Access the name of the current instance of the class
        print(f"Hello from {self.name}!" + "\n" + "Student in Information Technology at Linköpings University" + "\n" +"My idea is to write every day in the same class (class AdventOfCode)."
              + "\n" + "Each day's code will then be able to run through an instance variable created in the DriverClass." + "\n"*5)

    # ---------------------------------- advent of code 2022 day 1 task 1 ------------------------------------------
    def biggest_item(self, s: str) -> int:

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
    def biggest_3_items(self, s: str) -> int:
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
        #print(sumList)

        # add the sums together of the three highest values
        return sumList[0] + sumList[1] + sumList[2]




