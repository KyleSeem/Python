# Program prompts the user ten times for a test score between 60 and 100.
# Program displays the grade of each score upon entry.
# Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

scores = [] #will compile the values from userInput into a list
def finalGrades(scores):
    x = 1 #identifies entry index (starts at 1 for user)
    for grade in scores:
        if grade < 70:
            print 'Entry #{}:'.format(x), int(grade), '- Final grade: D'
            x = x+1
        elif grade < 80:
            print 'Entry #{}:'.format(x), int(grade), '- Final grade: C'
            x = x+1
        elif grade < 90:
            print 'Entry #{}:'.format(x), int(grade), '- Final grade: B'
            x = x+1
        else:
            print 'Entry #{}:'.format(x), int(grade), '- Final grade: A'
            x = x+1

def getScores():
    x = 1 #keeps track of entry and displays with each round of prompts
    while len(scores) < 10:
        try: #{} = place holder for x, statement uses float to allow for decimals
            userInput = float(raw_input('Please enter score #{} (must be between 60 and 100): '.format(x)))
        except ValueError: #errors for entry other than number, including null
            print 'Error: Invalid entry, please try again.'
        else:
            if(not 60 <= userInput <= 100): #requires number between 60 and 100
                # return userInput
                print 'Error: Invalid entry, please try again. '
            else:
                scores.append(userInput)
                print 'Entry Accepted'
                x = x+1
    finalGrades(scores)

getScores()
