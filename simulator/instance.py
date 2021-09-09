# -*- coding: utf-8 -*-
import logging
import numpy as np


class Instance():
    def __init__(self, sim_setting):
        logging.info("starting simulation...")
        self.max_size = sim_setting['knapsack_size']

        # set of supplier: M index by i
        self.suppliers = sim_setting['num_suplliers']

        # set of products: K index by k
        self.products = sim_setting['num_products']

        # set of lambda
        self._lambda = sim_setting['lambda']

        # set of basic price for each products
        self.b_price = np.around(np.random.uniform(
            sim_setting['b_price_low'],
            sim_setting['b_price_high'],
            sim_setting['num_products']
        ),2)

        self.n_items = sim_setting['n_items']

        self.sizes_ss = np.around(np.random.uniform(
            sim_setting['low_size'],
            sim_setting['high_size'],
            sim_setting['n_items']
        ))
        self.max_size_ss = sim_setting['knapsack_size']

        self.n_products = np.around(np.random.uniform(
            sim_setting['low_products'],
            sim_setting['high_products'],
            sim_setting['n_products']
        ))

        logging.info(f"max_size: {self.max_size}")
        logging.info(f"sizes: {self.sizes}")
        logging.info(f"profits: {self.profits}")
        logging.info(f"n_items: {self.n_items}")
        logging.info(f"sizes_ss: {self.sizes_ss}")
        logging.info(f"max_size_ss: {self.max_size_ss}")
        logging.info(f"max_size_ss: {self.n_products}")
        logging.info("simulation end")

    def get_data(self):
        logging.info("getting data from instance...")
        return {
            "profits": self.profits,
            "sizes": self.sizes,
            "max_size": self.max_size,
            "n_items": self.n_items,
            "sizes_ss": self.sizes_ss,
            "max_size_ss": self.max_size_ss,
            "n_products": self.n_products
        }
