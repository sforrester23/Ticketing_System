import sys

TICKET_PRICE = 10
SERVICE_CHARGE = int(2)

tickets_remaining = 100


# Create the calculate_price function. It takes number of tickets and returns: number_tickets * TICKET_PRICE
def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


# Run this code continuously until we run out of tickets
# How many tickets are remaining, using the tickets_remaning variable.

while tickets_remaining >= 1:

    print("There are {} tickets_remaining".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable.
    name = input("What is your name?  ")

    # Prompt the user by name, and ask how many tickets they would like.
    # Expect a ValueError to happen and handle it appropriately. Remember to test it out.
    try:
        number_tickets = input("Hey, {}, how many tickets would you like to purchase?  ".format(name))
        number_tickets = int(number_tickets)
        # Make sure the user cannot buy more tickets than there are
        if number_tickets > tickets_remaining:
            # Notify the user that the tickets have sold out
            raise ValueError(
                "Sorry, we do not have enough tickets to complete that transaction. The number of tickets we have left is {}. You may only purchase that many.".format(
                    tickets_remaining))
    except ValueError as err:
        print(
            "Oh no: that's not a valid value for the number of tickets you'd like to purchase! Please enter a valid number.")
        print("{}".format(err))
    else:

        # Calculate the price (number of tickets * price) and assign to variable
        total_cost = calculate_price(number_tickets)

        # Output price to screen
        print(
            "{}, you have selected {} tickets. Your total price for the amount of tickets you would like to buy is: ${}.".format(
                name, number_tickets, total_cost))

        # Ask if the user wants to proceed with the purchase. Y/N?
        confirmation = input("Would you like to proceed with this purchase, {}?  (Yes/No)  ".format(name))
        confirmation = confirmation.lower()
        # If they want to proceed,
        if confirmation == "yes":
            # print to screen "SOLD!" to confirm purchase,
            # TODO: gather credit card information and process.
            print("SOLD! Thank you for your purchase, {}.".format(name))
            # reduce the number of tickets available by the amount purchased.
            tickets_remaining = tickets_remaining - number_tickets

        # Otherwise, thank them by name
        else:
            print("Thank you anyway, {}. Come back soon to confirm your order!".format(name))

sys.exit(
    "Sorry, we have run out of tickets.")  # Cease the code if you run out of tickets i.e. the while loop no longer runs.
