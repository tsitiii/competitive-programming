# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.products = [1]  # Prefix product list with a dummy 1
        self.last_zero = -1  # Index of the last zero encountered

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]  # Reset because product resets after 0
            self.last_zero = len(self.products) - 1  # Store last zero index
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.products): 
            return 0
        if self.last_zero >= len(self.products) - k: 
            return 0
        return self.products[-1] // self.products[-k-1]  
