"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        """
        constructs an empty bidders list, highest bid and highest bidder
        """
        self._bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    @property
    def bidders(self):
        """
        gets the bidders
        :return: a list of bidders
        """
        return self._bidders

    @property
    def highest_bidder(self):
        """
        sets/gets the highest bidder
        :return: String
        """
        return self._highest_bidder

    @property
    def highest_bid(self):
        """
        gets the highest bid
        :return: float
        """
        return self._highest_bid

    def start_bid(self, bid):
        """
        sets the starting bid
        :param bid: float
        :return: None
        """
        self._highest_bid = bid

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders.clear()
        self._highest_bidder = 0

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            bidder(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self._highest_bid:
            print(f"{bidder} bid {'${:,.2f}'.format(bid)} in response to "
                  f"{self._highest_bidder}'s bid of "
                  f"{'${:,.2f}'.format(self._highest_bid)}!")
            self._highest_bid = bid
            self._highest_bidder = bidder
            self._notify_bidders()


class Bidder:

    def __init__(self, name, budget=100, bid_probability=None, bid_increase_perc=1.1):
        """
        constructs a bidder
        :param name: String
        :param budget: float
        :param bid_probability: float
        :param bid_increase_perc: float
        """
        self._name = name
        self._bid_probability = bid_probability
        self._budget = budget
        self._bid_increase_perc = bid_increase_perc
        if self._bid_increase_perc < 1:
            self._bid_increase_perc = 1.1
        self._highest_bid = 0
        if self._bid_probability is None:
            self._bid_probability = random.random()

    @property
    def name(self):
        """
        sets/gets the name of the bidder
        :return: String
        """
        return self._name

    @property
    def budget(self):
        """
        sets/gets the budget of the bidder
        :return: float
        """
        return self._budget

    @property
    def bid_probability(self):
        """
        sets/gets the probability of getting the bid
        :return: float
        """
        return self._bid_probability

    @property
    def bid_increase_perc(self):
        """
        sets/gets the bid increase percent
        :return: float
        """
        return self._bid_increase_perc

    @property
    def highest_bid(self):
        """
        sets/gets the highest bid
        :return: float
        """
        return self._highest_bid

    def check_bidder(self, auctioneer: Auctioneer):
        """
        checks if the bid is against another bidder and not against themselves.
        :param auctioneer: Auctioneer
        :return: boolean
        """
        return auctioneer.highest_bidder is not self

    def check_bid(self, auctioneer: Auctioneer):
        """
        checks if the bid is within the budget and higher than the highest bid.
        :param auctioneer: Auctioneer
        :return: boolean
        """
        bid = auctioneer.highest_bid * self._bid_increase_perc
        return self._budget >= auctioneer.highest_bid

    def check_probability(self):
        """
        checks if the bidder is going to get the bid or not.
        :return: boolean
        """
        prob = random.random()
        return self._bid_probability >= prob

    def make_new_bid(self, auctioneer):
        """
        makes offering bid to auctioneer.
        :param auctioneer: Auctioneer
        :return: None
        """
        bid = auctioneer.highest_bid * self._bid_increase_perc
        self._highest_bid = bid

    def __call__(self, auctioneer):
        """
        calls back the bidder object with an auctioneer passed
        :param auctioneer: Auctioneer
        :return: None
        """
        if self.check_bidder(auctioneer) and self.check_bid(auctioneer) and self.check_probability():
            self.make_new_bid(auctioneer)
            auctioneer.accept_bid(auctioneer.highest_bid * self._bid_increase_perc, self)

    def __str__(self):
        """
        shows the string representation of the bidder information
        :return:
        """
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        if bidders is None:
            self._bidders = []
        self._bidders = bidders

    def register_bidders(self, auctioneer: Auctioneer):
        for bidder in self._bidders:
            auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, starting_price, auctioneer: Auctioneer):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :type auctioneer: Auctioneer
        :param starting_price: float
        :param item: String
        :param auctioneer: auctioneer
        """
        print(f"\nAuctioning {item} starting at"
              f" {'${:,.2f}'.format(starting_price)}")
        self.register_bidders(auctioneer)
        auctioneer.start_bid(starting_price)
        for bidder in self._bidders:
            auctioneer.register_bidder(bidder)

        auctioneer.start_bid(starting_price)

        for bidder in self._bidders:
            bidder(auctioneer)

        print(f"\nThe winner of this auction is: "
              f"{auctioneer.highest_bidder} at"
              f" {'${:,.2f}'.format(auctioneer.highest_bid)}!\n")
        print("\n")

        highest_bids = {bidder.name: bidder.highest_bid for bidder in
                        auctioneer.bidders}
        print("Highest Bids per Bidder")
        for bidder, bid in highest_bids.items():
            print(f"Bidder: {bidder} Highest bid:"
                  f" {'${:,.2f}'.format(bid)}")


def main():
    bidders = []

    item = input("Item Name: ")
    price = int(input("Starting Price: "))

    print("Do you want to use hardcoded bidders or new custom bidders?")
    print("1. Load hardcoded bidders")
    print("2. Begin adding custom bidders")

    choice = int(input())

    while choice != 1 or 2:
        try:
            if choice == 1:
                bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
                bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
                bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
                bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
                bidders.append(Bidder("Scott", 4000, random.random(), 2))
                break
            elif choice == 2:
                print("How many bidders are there?: ")
                num_of_bidders = int(input())
                for bid in range(num_of_bidders):
                    print("Bidder Name: ")
                    name = input()
                    print("Bidder Budget: ")
                    budget = int(input())
                    bidders.append(Bidder(name, budget))
                break
            else:
                print("Please choose one of the options provided!")
                choice = int(input())
        except ValueError as e:
            print(e)

    print("\n\nStarting Auction!!")
    print("------------------")

    auctioneer = Auctioneer()
    my_auction = Auction(bidders)
    my_auction.simulate_auction(item, price, auctioneer)


if __name__ == '__main__':
    main()
