
import numpy as np

"""Problem statement:
March 26, THI $60 * 100 shares = $6000
Short Sell: 


"""

class OptionAnalysis():
    def __init__(self, current_price, option_call_dict, option_put_dict, future_price_list):
        self.current_price = current_price

        self.option_call_dict = option_call_dict
        self.option_put_dict = option_put_dict

        self.low_boundary = 1
        self.high_boundary = 4
        self.numb_sample = 31

        self.future_price_list = future_price_list

        # self.print_sell_short_profit()
        # self.print_option_call_profit()
        self.print_option_put_profit()


    def print_sell_short_profit(self):
        print("future price | short sell profit")

        for future_price in self.future_price_list:
            short_sell_profit = self.get_short_sell_profit(self.current_price, future_price)
            print('{0:12.03f} {1:12.03f}'.format(future_price, short_sell_profit))

    def print_option_call_profit(self):
        print("option call profit / strike price for July 17, 2015")

        header = "future price | "
        for strike_price in sorted(self.option_call_dict.keys()):
            # header += str(strike_price).ljust(12) + "| "
            header += "{0:10.03f}".format(strike_price) + " |"
        print(header)


        for future_price in self.future_price_list:
            line = "{0:12.03f}".format(future_price)+" "

            has_non_zero_value = False

            for strike_price in sorted(self.option_call_dict.keys()):

                profit = self.get_buy_call_profit(0, future_price, strike_price, self.option_call_dict[strike_price])

                if(profit != 0):
                    has_non_zero_value = True

                line += "{0:12.03f}".format(profit)

            if(has_non_zero_value):
                print(line)

    def print_option_put_profit(self):
        print("option put profit / strike price for July 17, 2015")

        header = "future price | "
        for strike_price in sorted(self.option_put_dict.keys()):
            # header += str(strike_price).ljust(12) + "| "
            header += "{0:10.03f}".format(strike_price) + " |"
        print(header)


        for future_price in self.future_price_list:
            line = "{0:12.03f}".format(future_price)+" "

            has_non_zero_value = False

            for strike_price in sorted(self.option_put_dict.keys()):

                profit = self.get_buy_put_profit(0, future_price, strike_price, self.option_put_dict[strike_price])

                if(profit != 0):
                    has_non_zero_value = True

                line += "{0:12.03f}".format(profit)

            if(has_non_zero_value):
                print(line)

    def get_short_sell_profit(self, price_old, price_new):
        return (price_old - price_new)

    def get_buy_call_profit(self, price_old, price_new, strike_price, quote):
        result = (price_new - strike_price - quote)
        if(result < -1 * quote):
            return -1 * quote
        return result

    def get_buy_put_profit(self, price_old, price_new, strike_price, quote):
        result = (strike_price - price_new - quote)
        if(result < -1 * quote):
            return -1 * quote
        return result



# option_call_dict = dict()
# option_call_dict[1.0] = 2.08
# option_call_dict[1.5] = 0.82
# option_call_dict[2] = 0.37
# option_call_dict[2.5] = 0.13
# option_call_dict[3] = 0.04
# option_call_dict[3.5] = 0.03

# option_put_dict = dict()
# # option_put_dict[1] = 0.03
# option_put_dict[1.5] = 0.02
# option_put_dict[2] = 0.09
# option_put_dict[2.5] = 0.32
# option_put_dict[3] = 0.74
# option_put_dict[3.5] = 1.05
# option_put_dict[4] = 1.5
# # option_put_dict[4.5] = 2.05
# # option_put_dict[5] = 2.34
# # option_put_dict[5.5] = 3.22


# future_price_list = np.hstack((np.linspace(1, 5, 41)))

# AMD = OptionAnalysis(2.3, option_call_dict, option_put_dict, future_price_list)

