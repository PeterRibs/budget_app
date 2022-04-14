def truncate(n):
    multiplier = 10
    return int(n * multiplier)/multiplier

def getTotals (categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map (lambda x: truncate(x/total), breakdown))
    return rounded
    
def create_spend_chart(categories):
    
    res = "Percentage spent by category\n" 
    
    i = 100
    totals = getTotals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        res += str(i).rjust(3) + "|" + cat_spaces + ('\n')
        i-=10
        
    lines = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    
    for category in categories:
        names.append(category.categoryName)
    
    maxi = max(names, key=len)
    
    for i in range(len(maxi)):
        nameStr = ' '*5
        for name in names:
            if i >= len(name):
                nameStr += " "*3
            else:
                nameStr += name[i] + " "*2
        
        if (i != len(maxi)-1):
            nameStr += '\n'
     
        x_axis += nameStr
    
    res += lines.rjust(len(lines)+4) + "\n" + x_axis
    return res