# -*- coding: utf-8 -*-
import logging
import numpy as np


class Instance():
    def __init__(self, sim_setting):
        logging.info("starting simulation...")
        # self.max_size = sim_setting['knapsack_size']

        # set of supplier: M index by i
        self.suppliers = sim_setting['num_suppliers']

        # set of products: K index by k
        self.products = sim_setting['num_products']

        # set of lambda
        self._lambda = sim_setting['lambda']

        # set of basic price for each products
        self.b_price = np.around(np.random.uniform(
            sim_setting['b_price_low'],
            sim_setting['b_price_high'],
            sim_setting['num_products']
        ), 2)

        # set of available quantity for each product k sold by supplier q_ki
        self.av_quantity = np.around(np.random.uniform(
            sim_setting['av_quantity_l'],
            sim_setting['av_quantity_h'],
            (sim_setting['num_products'], sim_setting['num_suppliers'])
        ))

        # set of price of each product of each supplier f_ki
        self.product_price = [np.around(np.random.uniform(
            0.9*self.b_price[k],
            1.1*self.b_price[k],
            sim_setting['num_suppliers']
            ), 2)
            for k in np.arange(0, sim_setting['num_products'])
        ]

        # set of penalty price F_K
        self.penalty_price = [np.around(
            1.2 * max(self.product_price[k]), 2)
            for k in np.arange(sim_setting['num_products'])
        ]

        # set of demand d_k for each product
        d_had_k = [sim_setting['lambda'] * max(self.av_quantity[k]) + \
                   (1 - sim_setting['lambda']) * sum(self.av_quantity[k])
                   for k in np.arange(sim_setting['num_products'])
                   ]

        self.demand = [np.round(
            d_had_k[k] - ((d_had_k[k] - 1) * self.b_price[k] / max(self.b_price))
        )
            for k in np.arange(sim_setting['num_products'])
        ]




        # self.n_items = sim_setting['n_items']
        #
        # self.sizes_ss = np.around(np.random.uniform(
        #     sim_setting['low_size'],
        #     sim_setting['high_size'],
        #     sim_setting['n_items']
        # ))
        # self.max_size_ss = sim_setting['knapsack_size']
        #
        # self.n_products = np.around(np.random.uniform(
        #     sim_setting['low_products'],
        #     sim_setting['high_products'],
        #     sim_setting['n_products']
        # ))
        #
        # logging.info(f"max_size: {self.max_size}")
        # logging.info(f"sizes: {self.sizes}")
        # logging.info(f"profits: {self.profits}")
        # logging.info(f"n_items: {self.n_items}")
        # logging.info(f"sizes_ss: {self.sizes_ss}")
        # logging.info(f"max_size_ss: {self.max_size_ss}")
        # logging.info(f"max_size_ss: {self.n_products}")
        # logging.info("simulation end")

    def get_data(self):
        logging.info("getting data from instance...")
        return {
            "suppliers": self.suppliers,
            "products": self.products,
            "av_quantity": self.av_quantity,
            "product_price": self.product_price,
            "penalty_price": self.penalty_price,
            "demand": self.demand,
            # "n_products": self.n_products
        }
