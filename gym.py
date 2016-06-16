# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

from decimal import *


class Gym:

    pricePerMonth = 0.0

    visitsPerWeek = 0

    payPerVisit = 0.0

    minutesPerVisit = 0

    def subscription_cost_per_visit(self):
        getcontext().prec = 3
        return Decimal(self.pricePerMonth) / (Decimal(self.visitsPerWeek) * 4)

    def subscription_total_cost(self):
        return Decimal(self.pricePerMonth)

    def pay_per_use_cost_per_visit(self):
        return Decimal(self.payPerVisit)

    def pay_per_use_total_cost(self):
        return Decimal(self.payPerVisit) * (Decimal(self.visitsPerWeek) * 4)

    def total_saved_per_month(self):
        return Decimal(self.payPerVisit) * (Decimal(self.visitsPerWeek) * 4) - Decimal(self.pricePerMonth)

    def cost_per_minute(self, pay_type):
        if pay_type == 'per_visit':
            return (Decimal(self.payPerVisit) * 100) / Decimal(self.minutesPerVisit)
        else:
            return (self.subscription_cost_per_visit() * 100) / Decimal(self.minutesPerVisit)

gym = Gym()
gym.pricePerMonth = input("How much is the monthly subscription fee? ")
gym.visitsPerWeek = input("How many gym visits in a week? ")
gym.payPerVisit = input("How much does it cost to use the gym on pay per use? ")
gym.minutesPerVisit = input("How many minutes do you spend at the gym each session? ")

print('\n')
print('Subscription cost per visit: £', gym.subscription_cost_per_visit())
print('Pay per use: £', gym.pay_per_use_cost_per_visit())

print('Subscription monthly cost: £', gym.subscription_total_cost())
print('Pay per use monthly cost: £', gym.pay_per_use_total_cost())

print('Saving each month: £', gym.total_saved_per_month())

print('Cost in pence per minute for subscription: ', gym.cost_per_minute('subscription'))
print('Cost in pence per minute for pay per use: ', gym.cost_per_minute('per_visit'))