import sys
class Sol2:
    # @param A : array of prices
    # @return an integer
    def maxProfit(self, price):
        maxprofit = 0
        globalmin = sys.maxint
        for i in range(len(price)):
            if price[i] < globalmin:
                globalmin = price[i]
            if (price[i] - globalmin) > maxprofit:
                maxprofit = price[i] - globalmin
        return maxprofit

import sys
class Buy2:
    # Strategy: trigger a buy whenever a minimum occurs
    # Tigger a sell whenever a maximum occurs
    def maxProfit(self, price):
        profit = 0
        curr_profit = 0
        curr_min = sys.maxint
        for i in range(len(price)):
            if price[i] < curr_min:
                curr_min = price[i]
            if (price[i] - curr_min) > curr_profit:
                curr_profit = price[i] - curr_min
            if (i > 1) and (price[i] < price[i-1]):
                # Sell at i-1, lock in profit!
                profit += curr_profit
                curr_profit = 0
                curr_min = price[i]
        # lock in any remaining profits
        profit += curr_profit
        return profit


def main():
    sol = Buy2()
    print(sol.maxProfit([1,2,3,0,2,7,3,3,3,4]))
main()

