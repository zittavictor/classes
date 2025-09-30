"""
Module: pay_stub.py
Developer: Your Name
Date Created: 2025-09-30
Date Last Modified: 2025-09-30
Description: Defines the Pay_Stub class with payroll calculations and summary tracking.
"""

FED_TAX = 0.1149
STATE_TAX = 0.0581
SS_TAX = 0.062
MED_TAX = 0.0145

class Pay_Stub:
    __total_stubs = 0
    __total_gross = 0
    __total_net = 0

    def __init__(self, name, hours, rate):
        self.__name = name
        self.__hours = hours
        self.__rate = rate
        self.__net = self.__calculate_net()

    def __calculate_net(self):
        gross = self.__hours * self.__rate
        fed_tax = gross * FED_TAX
        state_tax = gross * STATE_TAX
        ss_tax = gross * SS_TAX
        med_tax = gross * MED_TAX
        net = gross - (fed_tax + state_tax + ss_tax + med_tax)

        self.__increment_totals(gross, net)
        return net

    @classmethod
    def __increment_totals(cls, gross, net):
        cls.__total_stubs += 1
        cls.__total_gross += gross
        cls.__total_net += net

    @classmethod
    def __average_net(cls):
        if cls.__total_stubs == 0:
            return 0
        return cls.__total_net / cls.__total_stubs

    @classmethod
    def summary(cls):
        return (f"Total Number of Pay Stubs: {cls.__total_stubs}\n"
                f"Total Gross Pay: ${cls.__total_gross:.2f}\n"
                f"Total Net Pay: ${cls.__total_net:.2f}\n"
                f"Average Net Pay: ${cls.__average_net():.2f}")

    def __str__(self):
        return (f"Employee Name: {self.__name}\n"
                f"Hours Worked: {self.__hours}\n"
                f"Pay Rate: ${self.__rate:.2f}\n"
                f"Net Pay: ${self.__net:.2f}")
