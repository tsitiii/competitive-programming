# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class BrowserHistory(object):
    def __init__(self, homepage):
        """
        Initializes the browser history with the given homepage.
        :type homepage: str
        """
        self.back_stack = [homepage]  # Stack for back history
        self.forward_stack = []        # Stack for forward history
        self.current_index = 0         # Track the current page index

    def visit(self, url):
        """
        Visits a new URL from the current page.
        Clears the forward history.
        :type url: str
        :rtype: None
        """
        # Clear the forward history and add the new URL
        self.back_stack = self.back_stack[:self.current_index + 1]  # Keep history up to the current index
        self.back_stack.append(url)  # Add the new URL
        self.current_index += 1       # Move the current index forward
        self.forward_stack = []        # Reset the forward stack

    def back(self, steps):
        """
        Moves back in history by the given number of steps.
        If unable to go back that far, return the earliest URL.
        :type steps: int
        :rtype: str
        """
        # Move steps back in the history
        self.current_index = max(0, self.current_index - steps)  # Ensure we don't go before the start
        return self.back_stack[self.current_index]  # Return the current URL

    def forward(self, steps):
        """
        Moves forward in history by the given number of steps.
        If unable to go forward that far, return the latest URL.
        :type steps: int
        :rtype: str
        """
        # Move steps forward in the history
        self.current_index = min(len(self.back_stack) - 1, self.current_index + steps)  # Ensure we don't go beyond the end
        return self.back_stack[self.current_index]  # Return the current URL

# Example usage
if __name__ == "__main__":
    obj = BrowserHistory("leetcode.com")
    obj.visit("google.com")   # Current: google.com
    obj.visit("facebook.com")  # Current: facebook.com
    print(obj.back(1))         # Returns: google.com
    print(obj.back(1))         # Returns: leetcode.com
    print(obj.forward(1))      # Returns: google.com
    obj.visit("youtube.com")    # Current: youtube.com
    print(obj.forward(2))      # Returns: youtube.com
    print(obj.back(2))         # Returns: leetcode.com
    print(obj.back(7))         # Returns: leetcode.com (can't go back further)