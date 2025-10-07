import os


# Helper function to clear the screen (works on Windows, macOS, and Linux)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Store all bids
bids = {}

# Start bidding loop
while True:
    print("Welcome to the Secret Auction!")
    name = input("What's your name? ")
    bid = float(input("Write your bid: $"))

    # Save data into dictionary
    bids[name] = bid

    # Ask if there's another bidder
    new_bid = input("Type 'y' if there's another person who wants to bid, or 'n' to stop: ").lower()

    if new_bid == 'y':
        clear()  # hide previous bids
    else:
        break

# Find the highest bidder
highest_bidder = max(bids, key=bids.get)
print("\n🏆 The auction has ended! 🏆")
print(f"The winner is {highest_bidder} with a bid of ${bids[highest_bidder]:.2f}")
