import numpy as np
import json


fp = open("./etc/sim_setting.json", 'r')
sim_setting = json.load(fp)
fp.close()
a = sim_setting['num_suppliers']
b = np.around(np.random.uniform(
            sim_setting['b_price_low'],
            sim_setting['b_price_high'],
            sim_setting['num_products']
       ), 2)
print(b)