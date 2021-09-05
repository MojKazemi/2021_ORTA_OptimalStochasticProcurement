# -*- coding: utf-8 -*-
import time
import logging
import gurobipy as gp
from gurobipy import GRB


class SimpleKnapsack():
    def __init__(self):
        pass

    def solve(
        self, dict_data, reward, n_scenarios, time_limit=None,
        gap=None, verbose=False
    ):
        items = range(dict_data['n_items'])
        scenarios = range(n_scenarios)

        problem_name = "SimpleKP"
        logging.info("{}".format(problem_name))
        # logging.info(f"{problem_name}")

        model = gp.Model(problem_name)
        # x_i =1 : if purchasing contract is activated with supplier i as M
        X = model.addVars(
            dict_data['n_contract'],
            lb=0,
            ub=1,
            vtype=GRB.INTEGER,
            name='X'
        )

        # z_ikr : units of product  k as K purchased from i as M_k in interval r as R_i..
        #  .. and yielding a discount rate delta_ir
        Z = model.addvars(
            dict_data['n_product'],
            ib=0,
            ub=None,
            vtype=GRB.INTEGER,
            name='Z'
        )

        # Y if supplier i as M applied the discount  interval r as Ri
        Y = model.addVars(
            dict_data['n_discount'], n_scenarios,
            lb=0,
            ub=1,
            vtype=GRB.INTEGER,
            name='Y'
        )
        
        obj_funct = gp.quicksum(dict_data["profits"][i] * X[i] for i in items)
        # for s in scenarios:
        #     obj_funct += gp.quicksum(reward[i, s] * Y[i, s] for i in items)/(n_scenarios + 0.0)
        obj_funct += gp.quicksum(reward[i, s] * Y[i, s] for i in items for s in scenarios)/(n_scenarios + 0.0)
        model.setObjective(obj_funct, GRB.MINIMIZE)   # make minimize Objective Function

        model.addConstr(
            gp.quicksum(dict_data['sizes'][i] * X[i] for i in items) <= dict_data['max_size'],
            f"volume_limit_fs"
        )
        
        for s in scenarios:
            model.addConstr(
                gp.quicksum(dict_data['sizes_ss'][i] * Y[i, s] for i in items) <= dict_data['max_size_ss'],
                f"volume_limit_ss_{s}"
            )
        for i in items:
            model.addConstr(
                gp.quicksum(Y[i, s] for s in scenarios) <= n_scenarios * X[i],
                f"link_X_Y_for_item_{i}"
            )
        model.update()
        if gap:
            model.setParam('MIPgap', gap)
        if time_limit:
            model.setParam(GRB.Param.TimeLimit, time_limit)
        if verbose:
            model.setParam('OutputFlag', 1)
        else:
            model.setParam('OutputFlag', 0)
        model.setParam('LogFile', './logs/gurobi.log')
        # model.write("./logs/model.lp")

        start = time.time()
        model.optimize()
        end = time.time()
        comp_time = end - start
        
        sol = [0] * dict_data['n_items']
        of = -1
        if model.status == GRB.Status.OPTIMAL:
            for i in items:
                grb_var = model.getVarByName(
                    f"X[{i}]"
                )
                sol[i] = grb_var.X
            of = model.getObjective().getValue()
        return of, sol, comp_time
