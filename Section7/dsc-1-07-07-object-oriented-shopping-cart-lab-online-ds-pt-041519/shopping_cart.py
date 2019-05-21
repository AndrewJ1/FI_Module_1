class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.employee_discount = emp_discount
        self.total = 0
        self.items =[]
        
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({'name': name, 'price': price})
            self.total += price
        return self.total
    
    def mean_item_price(self):
        return self.total / len(self.items)

    def median_item_price(self):
        # sort price list; length of list; find middle if even; find middle if odd
        prices  = []
        for item in self.items:
            prices.append(item['price'])
        prices.sort()
        length = len(prices)
        if length % 2 == 0:
            middle_a = int(length/2)
            middle_b = middle_a -1
            median = (prices[middle_a] + prices[middle_b])/2
            return median
        else:
            middle = int(length/2)
            return prices[middle]
      
             

    def apply_discount(self):
        if self.employee_discount != None:
            discount = self.total * ((100 - self.employee_discount)/100)
            return discount
        else:
            return "Sorry, there is no discount to apply to your cart :("
        

    def void_last_item(self):
        if self.items != []:
            removed = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed['price']
