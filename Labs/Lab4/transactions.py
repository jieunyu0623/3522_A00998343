class Transactions:

    def __init__(self, date_recorded, dollar, budget_category, description):
        self._date_recorded = date_recorded
        self._dollar = dollar
        self._budget_category = budget_category
        self._description = description

    def get_date_recorded(self):
        return self._date_recorded

    def get_dollar(self):
        return self._dollar

    def get_budget_category(self):
        return self._budget_category

    def get_description(self):
        return self._description

    def __str__(self):
        return f"Amount: {self.get_dollar()}\n" \
               f"Date: {self.get_date_recorded()}\n" \
               f"Description: {self.get_description()}\n"
