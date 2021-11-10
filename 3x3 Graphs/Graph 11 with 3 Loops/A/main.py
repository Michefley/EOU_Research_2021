import sympy as sp
import random as rd

#################################################################################
# Author: Michael Hefley
# Date: 11/10/2021
# Graph: 11 w/ 3 loops
# Nilpotent Signing: D
#
# Purpose: We wish to obtain a certain realization of our Signed Coefficient Support
# Arbitrary Pattern (SCSAP) of a specific graph (or signed graph). The program 
# generates random coefficients for our characteristic polynomial and then runs
# through every possible signing of the 3 coefficients and saves a desired 
# realization to the "outout.txt" file. Sections that may need to be changed 
# when switching to a different graph contain double asterisks around the comments 
# above that section. Remember, this program does NOT show if a graph is NOT
# SCSAP, but can show that it is if ALL 27 realizations are found.
#################################################################################

def main():
  a, b, c, d, e, f, g, u, v, w = sp.symbols("a b c d e f g u v w")

  # If you wish to clean up the file for a new run, uncomment the cleanFile() function below.
  cleanFile()

  # **Set the "free" variables with correct signing**
  c = 1
  d = 2

  trueVals = 0
  while True:
    # Chooses u,v,w to ba a random integer.
    uTemp = rd.randint(1,10)
    vTemp = rd.randint(1,10)
    wTemp = rd.randint(1,10)

    # **Ensure we eliminate all possibilities of dividing by 0 and obtaining imaginary numbers.**
    if (uTemp != (-c-2*d) and -1*uTemp != (-c-2*d)):
      for x in range(3): # (0,+,-) for the u value

        u = uTemp
        if (x==0): # Makes u = 0
          u = 0
          uStr = "0"
        elif (x==1): # Makes u positive
          u = abs(u)
          uStr = "+"
        else: # Makes u negative
          u = -1*abs(u)
          uStr = "-"

        for y in range(3): # (0,+,-) for the v value

          v = vTemp
          if (y==0): # Makes v = 0
            v = 0
            vStr = "0"
          elif (y==1): # Makes v positive
            v = abs(v)
            vStr = "+"
          else: # Makes v negative
            v = -1*abs(v)
            vStr = "-"

          for z in range(3): # (0,+,-) for the w value
           
            w = wTemp
            if (z==0): # Makes w = 0
              w = 0
              wStr = "0"
            elif (z==1): # Makes w positive
              w = abs(w)
              wStr = "+"
            else: # Makes w negative
              w = -1*abs(w)
              wStr = "-"

            # **Set variables to make coefficients of charpoly be u,v, and w.**
            e = -c-d-u
            b = (-2*c**2*u - 4*c*d*u - c*u**2 - c*v - 2*d**2*u - d*u**2 - d*v - u*v + w - (c + d)**3)/(c + 2*d + u)
            a = -(d**3 + d**2*u + d*v + w)/(c + 2*d + u)

            # **Creates matrix and sign pattern.**
            A = sp.Matrix([[c,1,b],[a,d,0],[1,0,e]])
            realizationPattern = "{" + uStr + "," + vStr + "," + wStr + "}"

            # Makes a copy of the file.
            with open("output.txt", 'r') as file:
              data = file.readlines()

            # **Checks to see if our variables have the correct signing and then checks to see
            # if the spot in the text file is taken for that realization pattern. If its not 
            # then we edit our copy of the file with our found realization then overwrite the 
            # actually file.**
            if (a < 0 and b < 0 and e < 0):
              if (data[5*(9*x + 3*y + z)] == '\n'):
                trueVals = trueVals + 1

                # **Section that writes to the copy of the file. 
                data[(5*(9*x + 3*y + z))] = "Realization " + realizationPattern + '\n'

                data[(1 + 5*(9*x + 3*y + z))] = "u = " + str(u) + ", v = " + str(v) + ", w = " + str(w) + '\n'

                data[(2 + 5*(9*x + 3*y + z))] = "a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) + ", d = " + str(d) + ", e = " + str(e) + '\n'

                data[(3 + 5*(9*x + 3*y + z))] = str(A.charpoly("x")) + '\n'

                # Overwrites the text file with our updated copy of the file that contains
                # a new realization.
                with open("output.txt", 'w') as file:
                  file.writelines(data)

                # If we have obtained 27 realizations, we may stop ALL of the loops and thus
                # quit the program.
                if (trueVals == 27):
                  return

# This method takes our text file and wipes it clean. Then it will create the neccesary
# number of newlines in the file so we can reference line numbers and check to see if 
# we have found that specific realization yet (if the line equals '\n').
def cleanFile():
  with open("output.txt", 'w'):
    pass

  with open("output.txt", 'a') as file:
    for i in range(0, 134):
      file.write('\n')

main()


                  





