#!/usr/bin/python

class Gym:

    pricePerMonth = 0.0

    visitsPerWeek = 0

    payPerVisit = 0.0

    minutesPerVisit = 0

    def subscription_cost_per_visit(self):
        print 'Subscription cost per visit: ', float(self.pricePerMonth) / float(self.visitsPerWeek * 4)

    def subscription_total_cost(self):
        print 'Subscription monthly cost: ', self.pricePerMonth

    def pay_per_use_cost_per_visit(self):
        print 'Pay per use: ', self.payPerVisit

    def pay_per_use_total_cost(self):
        print 'Pay per use monthly cost: ', float(self.payPerVisit) * float(self.visitsPerWeek * 4)

    def total_saved_per_month(self):
        print 'Saving each month: ', (float(self.payPerVisit) * float(self.visitsPerWeek * 4)) - float(self.pricePerMonth)

gym = Gym()
gym.pricePerMonth = input("How much is the monthly subscription fee? ")
gym.visitsPerWeek = input("How many gym visits in a week? ")
gym.payPerVisit = input("How much does it cost to use the gym on pay per use? ")
gym.minutesPerVisit = input("How many minutes do you spend at the gym each session? ")

gym.subscription_cost_per_visit()
gym.subscription_total_cost()
gym.pay_per_use_cost_per_visit()
gym.pay_per_use_total_cost()
gym.total_saved_per_month()
