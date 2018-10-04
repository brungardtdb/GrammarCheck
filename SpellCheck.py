'''**************************************************************
SpellCheck.py
Author: David Brungardt

This application prompts the user to enter a sentence.
If the first letter is capitalized and the sentence has punctuation, the
application will read back the sentence.
If the sentence lacks a capitalized first letter, the application will
add one.
If the sentence lacks punctuation, the application will add a period
to the end.
****************************************************************'''

class SpellCheck:

    #declare and initialize variables
    userSentence = "" # Original sentence
    counter  = 0; # use counter to simulate do-while loop so loop iterates >= 1 times

    ch = ' ' # Temporary character holder

    # define GrammarCheck function
    def GrammarCheck(userSentence):
        # capitalize first word in userSentence
        userSentence = userSentence[0].capitalize() + userSentence[1:]

        # check for punctuation at the end of userSentence
        ch = userSentence[-1:]

        # if there is no punctuation
        if ch != "." and ch != "!" and ch != "?":
            correctedSentence = userSentence + "."

        # if there is punctuation
        else:
            correctedSentence = userSentence

        # print corrected sentence
        print(correctedSentence)

    while userSentence.lower() != 'q':

        # if the user hasn't already entered a word
        if counter == 0:
            # Get sentence from user
            userSentence = input("Please enter a sentence: ")
            counter = counter + 1; # increase couter to activete other if statement
            if userSentence.lower() != "q":
                # if user wishes to continue, perform grammar check
                GrammarCheck(userSentence)

        # if the user has already entered a word
        elif counter > 0:
            # Get sentence from user
            userSentence = input("Enter another sentence or press 'Q' to quit:  ")
            if userSentence.lower() != "q":
                # if user wishes to continue, perform grammar check
                GrammarCheck(userSentence)
