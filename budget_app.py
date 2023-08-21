class Category:

    def __init__(self, category):
        self.ledger = []; self.category = category

    def __str__(self):
        result = self.category.center(30, "*") + "\n"
        for item in self.ledger:
            temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            result += temp + "\n"
        return result + "Total: " + str(self.get_balance())

    def deposit(self, amount, description=""):
        self.ledger.append({'amount':amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount':amount*-1, 'description': description})
            return True
        return False


    def get_balance(self):
        result = 0
        for item in self.ledger: result += item['amount']
        return result


    def transfer(self, amount, budget_cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budget_cat.category)
            budget_cat.deposit(amount, "Transfer from " + self.category)
            return True
        return False


    def check_funds(self, amount):
        if amount > self.get_balance(): return False
        else: return True


def create_spend_chart(categories):
    spend = []
    for category in categories:
        num = 0
        for item in category.ledger:
            if item['amount'] < 0: num += abs(item['amount'])
        spend.append(num)
    percentage = [i/sum(spend) * 100 for i in spend]

    result = "Percentage spent by category"
    for i in range(100, -1, -10):
        result += "\n" + str(i).rjust(3) + "|"
        for j in percentage:
            if j > i: result += " o "
            else: result += "   "
        result += " "
    result += "\n    " + '-' * 10

    cat_len = []
    for category in categories: cat_len.append(len(category.category))
    max_ = max(cat_len)

    for i in range(max_):
        result += "\n    "
        for j in range(len(categories)):
            if i < cat_len[j]: result += " " + categories[j].category[i] + " "
            else: result += "   "
        result += " "
    return result
