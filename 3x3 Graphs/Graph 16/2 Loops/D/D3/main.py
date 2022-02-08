import sympy as sp
import random as rd
import fractions as fr

#################################################################################
# Author: Michael Hefley
# Date: 11/18/2021
# Graph: 16 w/ 2 loops
# Nilpotent Signing: E

# Purpose: We wish to obtain a certain realization of our Signed Coefficient Support
# Arbitrary Pattern (SCSAP) of a specific graph (or signed graph). The program
# generates random coefficients for our characteristic polynomial and then runs
# through every possible signing of the 3 coefficients and saves a desired
# realization to the "output.txt" file. Sections that may need to be changed
# when switching to a different graph contain double asterisks around the comments
# above that section. Remember, this program does NOT show if a graph is NOT
# SCSAP, but can show that it is if ALL 27 realizations are found.
#################################################################################


def main():
    realization_chars = ['-', '0', '+']

    # If you wish to clean up the file for a new run, uncomment the cleanFile() function below.
    clean_file()

    # **Set the "free" variables with correct signing**
    b = fr.Fraction(1)
    c = fr.Fraction(-3)
    f = fr.Fraction(-2)

    while True:
        # Chooses u,v,w to ba a random integer.
        u_temp = fr.Fraction(rd.uniform(.001, 10.0))
        v_temp = fr.Fraction(rd.uniform(.001, 10.0))
        w_temp = fr.Fraction(rd.uniform(.001, 10.0))

        # **Ensure we eliminate all possibilities of dividing by 0 and obtaining imaginary numbers.**
        if b * c ** 2 - c * f - 1 != 0:
            for x, index1 in enumerate(realization_chars):  # (-,0,+) for the u value
                u = (x - 1) * u_temp

                for y, index2 in enumerate(realization_chars):  # (-,0,+) for the v value
                    v = (y - 1) * v_temp

                    for z, index3 in enumerate(realization_chars):  # (-,0,+) for the w value
                        w = (z - 1) * w_temp

                        # **Set variables to make coefficients of charpoly be u,v, and w.**
                        g = -f - u

                        d = (b ** 2 * c + b * c * f ** 2 + b * c * f * u + b * c * v - 2 * b * f - b * u - f ** 3 - f ** 2 * u - f * v - w) / (-b * c ** 2 + c * f + 1)
                        a = (-b * c * f - b * c * u + b - c * w + f ** 2 + f * u + v) / (b * c ** 2 - c * f - 1)

                        # **Creates matrix and sign pattern.**
                        matrix = sp.Matrix([[0, 1, a], [b, f, d], [1, c, g]])

                        # Makes a copy of the file.
                        with open("output.txt", 'r') as file:
                            data = file.readlines()

                        # **Checks to see if our variables have the correct signing and then checks to see
                        # if the spot in the text file is taken for that realization pattern. If its not
                        # then we edit our copy of the file with our found realization then overwrite the
                        # actually file.**
                        if a < 0 and d > 0 and g > 0:
                            if data[5 * (9 * x + 3 * y + z)] == '\n':

                                # **Section that writes to the copy of the file.
                                data[(5 * (9 * x + 3 * y + z))] = f'Realization {{{realization_chars[x]},' \
                                                                  f'{realization_chars[y]},' \
                                                                  f'{realization_chars[z]}}} \n'

                                data[(1 + 5 * (9 * x + 3 * y + z))] = f'{u = }, {v = }, {w = } \n'

                                data[(2 + 5 * (9 * x + 3 * y + z))] = f'{a = }, {b = }, {c = } {d = }, {f = }, {g = } \n'

                                data[(3 + 5 * (9 * x + 3 * y + z))] = f'{matrix.charpoly("x")} \n'

                                data[135] = str(int(data[135]) + 1)

                                # Overwrites the text file with our updated copy of the file that contains
                                # a new realization.
                                with open("output.txt", 'w') as file:
                                    file.writelines(data)

                                # If we have obtained 27 realizations, we may stop ALL of the loops and thus
                                # quit the program.
                        if int(data[135]) == 27:
                            return


# This method takes our text file and wipes it clean. Then it will create the necessary
# number of newlines in the file, so we can reference line numbers and check to see if
# we have found that specific realization yet (if the line equals '\n').
def clean_file():
    with open("output.txt", 'w'):
        pass

    with open("output.txt", 'a') as file:
        for i in range(135):
            file.write('\n')
            if i == 134:
                file.write('0')


main()
