'''The supermarket has previously had issues with discounts being set as values above 50.
Explain how encapsulation could be applied to the ItemForSale class to stop this problem from occurring.
You are not expected to write any code in your answer to this question.
'''
class ItemForSale:
    def __init__(self, itemName, price, discount):
        self.itemName = itemName
        self.price = price
        self.discount = discount

    def setDiscount(self, discount):
        if discount>50:
            return False
        else:
            self.discount = discount
            return True
        
myItem = ItemForSale("Posh Chocolate(100g)", 99.99, 0)

print(myItem.discount)

success = myItem.setDiscount(100)
if success:
    print("Item discount applied")
else: 
    print("Item discount invalid, max 50")