# let's go get some software that someone else wrote

import luhn  

# a function that uses the 'luhn' code - it takes a 'card_number' and returns 'true' or 'false' if the card is valid.

def is_credit_card_valid(card_number):    

    return luhn.verify(card_number)

# Let's tell the world whose awful credit card validator this is.

print ("Sarah Zemler Credit Card Validator")

# Let's get the card number from the user

card_number = input("Enter your 16-digit credit card number: ")

# Validate the credit card number using the Luhn algorithm

if is_credit_card_valid(card_number):           # we are calling the function above and sending it the card_number to validate

    print("The credit card number is valid.")

else:

    print("The credit card number is invalid.")

if len(card_number) == 15 and card_number.isdigit():     
    
    print ("Card is valid.")
<<<<<<< HEAD
=======
else:
    print ("Invalid card number. It must be 16 digits long.") 
>>>>>>> 145c2a18b65ce3a1426d9737a7b1cccb57f0f4c9

def run_tests():

    assert is_credit_card_valid("4111111111111111"), '4111111111111111 should pass but did not'

    assert is_credit_card_valid("5105105105105100"), '5105105105105100 should pass but did not'

    assert not is_credit_card_valid("134"), '134 should not pass but did'

    assert not is_credit_card_valid("1234567890123456"), '1234567890123456 should not pass but did'

    assert not is_credit_card_valid("000000000000"), 'This is a bad test and we will get an error message'

<<<<<<< HEAD
run_tests() 
=======
run_tests() 
>>>>>>> 145c2a18b65ce3a1426d9737a7b1cccb57f0f4c9
