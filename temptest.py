import numpy as np
import json
from simulator.instance import Instance


fp = open("./etc/sim_setting.json", 'r')
sim_setting = json.load(fp)
fp.close()
# a = sim_setting['num_suppliers']

inst = Instance(sim_setting)
dict_data = inst.get_data()

# print(dict_data['suppliers'])

# b_price = np.around(np.random.uniform(
#             sim_setting['b_price_low'],
#             sim_setting['b_price_high'],
#             sim_setting['num_products']
#         ), 2)
#
# av_quantity = np.around(np.random.uniform(
#             sim_setting['av_quantity_l'],
#             sim_setting['av_quantity_h'],
#             (sim_setting['num_products'], sim_setting['num_suppliers'])
#         ))
#
# product_price = [np.around(np.random.uniform(
#             0.9*b_price[k],
#             1.1*b_price[k],
#             sim_setting['num_suppliers']
#         ), 2) for k in np.arange(0 , sim_setting['num_products'])]
#
# penalty_price = [np.around(
#     1.2* max(product_price[k]),2)
#     for k in np.arange(sim_setting['num_products'])]
#
# d_had_k = [sim_setting['lambda'] * max(av_quantity[k]) + \
#            (1 - sim_setting['lambda']) * sum(av_quantity[k])
#            for k in np.arange(sim_setting['num_products'])
#            ]
#
# demand = [np.round(
#     d_had_k[k] - ((d_had_k[k] - 1) * b_price[k] / max(b_price))
#     )
#     for k in np.arange(sim_setting['num_products'])
# ]

# print('b_price=\n', b_price)
# print('av_quantity=\n', av_quantity[0][0])
# print('product_price=\n',product_price)
# a=[max(product_price[k]) for k in np.arange(sim_setting['num_products'])]
# print(a)
# print('penalty_price=\n', penalty_price)
# print(b_price)
# print(b_price[0])
# print(d_had_k)
# print('deman = \n', demand)

