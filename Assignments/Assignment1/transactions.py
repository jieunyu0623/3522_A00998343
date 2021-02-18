class Transactions:
    """
    transaction class used to record transaction information.
    """

    def __init__(self, date_recorded, dollar, description):
        """
        constructs a transaction with current time/date, amount and
        location/description.
        :param date_recorded: date
        :param dollar: float
        :param description: String
        """
        self._date_recorded = date_recorded
        self._dollar = dollar
        self._description = description

    def get_date_recorded(self):
        """
        gets the date recorded of a transaction.
        :return: date
        """
        return self._date_recorded

    def get_dollar(self):
        """
        gets the amount of a transaction.
        :return: float
        """
        return self._dollar

    def get_description(self):
        """
        gets the description of a transaction.
        :return: String
        """
        return self._description

    def __str__(self):
        """
        shows the string representation of transaction information.
        :return: String
        """
        return f"Amount: {self.get_dollar()}\n" \
               f"Date: {self.get_date_recorded()}\n" \
               f"Description: {self.get_description()}\n"
