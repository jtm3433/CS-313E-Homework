#  File: Bowling.py
#  Description: Calculates output score for bowling frames
#  Student's Name: John Mitchel
#  Student's UT EID: jtm3433
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 2/1/2016
#  Date Last Modified: 2/2/2016


# function that reads a line of data and prints a properly formatted line of the data
def setupFormat(strFormat):
    
    # establish intitial output frame reference values
    printMe= "|"
    frame = 1
    ballTwo = False


    # run through each item of data and perform appropriate actions
    for i in range(len(strFormat)):

        # check to see if function is in last frame of game so that special action may be taken
        if frame == 10:
            if(strFormat[i] == "X" or strFormat[i+1]=="/"):
                printMe += strFormat[i] + " " + strFormat[i+1] + " " + strFormat[i+2]                    
            else:
                printMe += "  " + strFormat[i] + " " + strFormat[i+1]
            printMe += "|"
            print(printMe)
            break

        # formatting for second ball of frame
        if ballTwo:
            printMe += " " + strFormat[i] + "|"
            ballTwo = False
            frame += 1
            continue

        # skip to the next frame for a strike
        if strFormat[i] == "X":
            printMe += (str(strFormat[i]))
            printMe += ("  |")
            frame += 1

        # first ball of frame
        else:
            printMe += strFormat[i]
            ballTwo = True

def calculateScore(strScore):
    # intialize variables
    score = 0
    printMe = "|"
    frame = 1
    ballTwo = False
    strike = False
    spare = False

    # run through each item of data and perform appropriate formatting/calculations
    for i in range(len(strScore)):
        # special action for last frame of game
        if frame == 10:
            
            # second to last frame was a strike
            # retroactively add score and finish formatting before continuing
            if strike:
                strike = False
                for j in range(i, i+2):                
                    if(strScore[j]=="X"):
                            score += 10
                    elif(strScore[j]=="/"):
                        score += 10-int(strScore[j-1])
                    elif(strScore[j]=="-"):
                        score += 0
                    else:
                        score += int(strScore[j])
                printMe += str(score).rjust(3) + "|"

            # second to last frame was a spare
            # retroactively add score and finish formatting before continuing
            if spare:
                if (strScore[i] != "-"):
                    if (strScore[i] == "X"):
                        score += 10
                    else:
                        score += int(strScore[i])
                printMe += str(score).rjust(3) + "|"

            # detect strike
            # self-contain remainder of necessary code due to special circumstances
            if(strScore[i]=="X"):
                if strScore[i+2] == "/":
                    score += 20
                elif strScore[i+1] == "X":
                    if strScore[i+2] == "X":
                        score += 30
                    elif strScore[i+2] == "-":
                        score += 20
                    else:
                        score += 20 + int(strScore[i+2])
                else:
                    score += int(strScore[i]) + int(strScore[i+1])
                printMe += str(score).rjust(5)
                printMe += "|"
                print(printMe)
                break

            # detect spare
            # self-contain remainder of necessary code due to special circumstances
            if(strScore[i+1]=="/"):
                score += 10
                if(strScore[i+2]=="X"):
                    score += 10
                elif(strScore[i+2]!="-"):
                    score += int(strScore[i+2])
                printMe += str(score).rjust(5)
                printMe += "|"
                print(printMe)
                break
                
            # check for presence of null bowl and react accordingly
            # if none found, convert data to ints and add to score
            if(strScore[i+1]=="-"):
                if(strScore[i]!="-"):
                    score += int(strScore[i])
            elif(strScore[i]=="-"):
                score += int(strScore[i+1])
            else:
                score += int(strScore[i+1]) + int(strScore[i])           
            
            # add score and format to printMe, print line, and exit function
            printMe += str(score).rjust(5)
            printMe += "|"
            print(printMe)
            break

        # last bowl was a strike
        # retroactively add data and formatting before calculating current frame
        if strike:
            strike = False
            for j in range(i, i+2):                
                if(strScore[j]=="X"):
                    score += 10
                elif(strScore[j]=="/"):
                    score += 10-int(strScore[j-1])
                elif(strScore[j]=="-"):
                    score += 0
                else:
                    score += int(strScore[j])
            printMe += str(score).rjust(3) + "|"
    
        # last bowl was a spare
        # retroactively add data and formatting before calculating current frame
        if spare:
            spare = False
            if(strScore[i]=="X"):
                score += 10
                strike = True
            else:
                score += int(strScore[i])
            printMe += str(score).rjust(3) + "|"            

        # second ball of frame
        if ballTwo:
            ballTwo = False
            
            # check for spare
            if (strScore[i] == "/"):
                if(strScore[i-1]=="-"):
                    score += 10
                else:
                    score += (10-int(strScore[i-1]))
                spare = True
                frame += 1
                continue

            # check for null
            # if no null, add data to score
            if (strScore[i] != "-"):
                score += int(strScore[i])

            # add score and formatting to printMe, go to next frame, and run next iteration
            printMe += str(score).rjust(3) + "|"
            frame += 1
            continue

        # first ball of frame
        # if null, do nothing and run next iteration for the second ball of the frame
        if strScore[i] == "-":
            ballTwo = True
            continue

        # check for strike
        if(strScore[i]=="X"):
            score += 10
            strike = True
            frame += 1
            continue

        # first ball of frame
        # no strike or null - add data to score and run iteration for second ball of frame
        score += int(strScore[i])
        ballTwo = True


def main():
    
    # set up initial frame output    
    print("  1   2   3   4   5   6   7   8   9    10")
    print("+---+---+---+---+---+---+---+---+---+-----+")

    # read in scores files    
    scores = open("scores.txt", "r")

    for line in scores:
        readMe = line.rstrip("\n")
        sendMe = ""

        # eliminates whitespace lines 
        for i in range(len(readMe)):
            if readMe[i] != " ":
                sendMe += readMe[i]

        # convert data into more readable format
        setupFormat(sendMe)

        # convert data into formatted score data
        calculateScore(sendMe)
        print("+---+---+---+---+---+---+---+---+---+-----+")


    
main()
