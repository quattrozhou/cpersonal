
import numpy as np

from OptionAnalysis import OptionAnalysis


option_call_dict = dict()
option_call_dict[1.0] = 2.08
option_call_dict[1.5] = 0.82
option_call_dict[2] = 0.37
option_call_dict[2.5] = 0.13
option_call_dict[3] = 0.04
option_call_dict[3.5] = 0.03


option_put_dict = dict()
# option_put_dict[1] = 0.03
option_put_dict[1.5] = 0.02
option_put_dict[2] = 0.09
option_put_dict[2.5] = 0.32
option_put_dict[3] = 0.74
option_put_dict[3.5] = 1.05
option_put_dict[4] = 1.5
# option_put_dict[4.5] = 2.05
# option_put_dict[5] = 2.34
# option_put_dict[5.5] = 3.22


future_price_list = np.hstack((np.linspace(1, 5, 41)))

AMD = OptionAnalysis(2.3, option_call_dict, option_put_dict, future_price_list)




# buy_put_profit = get_buy_put_profit(60, future_price, 60, 2)