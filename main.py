"""
@author: Shiva Shanker Reddy
Date: 14th July 2020
"""
import math


class Compound_interest:
    def __init__(self, p_amount, interest_rate, n_years):
        """
        
        self.p_amount: principal amount
        self.interest_rate: rate of interest
        self.n_years = number of years
        
        """
        self.p_amount = p_amount
        self.interest_rate = interest_rate
        self.n_years = n_years
    

    def compound_yearly(self):
        """

        formula: A = P * (1 + r)^n
        
        """
    
        final_amount = self.p_amount*(math.pow(
            1.0+(self.interest_rate/100),
            self.n_years)
            )

        return (round(final_amount, 2))
    

    def compound_frequencies(self, freq=4):
        """

        for quarterly n = 4(12/3)
            monthly n = 12
            semi-annualy n = 2(12/5)
            daily n= 365

        formula: A = P * (1 + r/n)^n*t
        
        """
        final_amount = self.p_amount*(math.pow(
            1+((self.interest_rate/100)/freq),
            (freq*self.n_years))
            )
        
        return(round(final_amount, 2))
