class Category():
    
    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.ledger = list()
        self.totalAmount = 0
        
    def __str__(self):
        spendList = list()
        categoryTitle = "%s\n"%self.categoryName.capitalize().center(30, "*")
        gastos = self.ledger
        spendList.append(categoryTitle)
        for i in range(0, len(gastos)):
            lenAmount = len(str(" {:.2f}".format(gastos[i]['amount'])))
            lenDescription = len(gastos[i]['description'])
            lenTotal = lenAmount + lenDescription
            spendItem = "{}{} {:.2f}\n".format(gastos[i]['description'][0:23]," "*(30-lenTotal), gastos[i]['amount'])
            spendList.append(spendItem)

        spendList.append("Total: {:.2f}".format(self.get_balance()))
        spendStr = "".join(spendList)
        return spendStr
        
    def deposit(self, amount, description = ""):
        '''A deposit method that accepts an amount and description. 
        If no description is given, it should default to an empty string. 
        The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.'''
        self.totalAmount += amount
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = ""):
        '''A withdraw method that is similar to the deposit method, but the amount passed in should be stored 
            in the ledger as a negative number. 
            If there are not enough funds, nothing should be added to the ledger. 
            This method should return True if the withdrawal took place, and False otherwise.'''
        if (self.check_funds(amount)):
            self.totalAmount -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        '''A get_balance method that returns the current balance of the budget category 
            based on the deposits and withdrawals that have occurred.'''
        totalCash = self.totalAmount
        return totalCash
    
    def transfer(self, amount, budgetCategory):
        '''A transfer method that accepts an amount and another budget category as arguments. 
            The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
            The method should then add a deposit to the other budget category with the amount and the description 
            "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. 
            This method should return True if the transfer took place, and False otherwise.'''
        if (self.check_funds(amount)):
            self.totalAmount -= amount
            self.ledger.append({'amount': -amount, 'description': "Transfer to %s"%budgetCategory.categoryName})
            budgetCategory.deposit(amount, description = "Transfer from %s"%self.categoryName)
            return True
        else:
            return False
        
    def check_funds(self, amount):
        '''A check_funds method that accepts an amount as an argument. 
            It returns False if the amount is greater than the balance of the budget category and returns True otherwise. 
            This method should be used by both the withdraw method and transfer method.'''
        if (amount > self.get_balance()):
            return False
        else:
            return True

    def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total
