import numpy as np

class MonteCarloSimulator:
    def __init__(self, monthly_returns, years, monthly_investment):
        self.monthly_returns = monthly_returns
        self.years = years
        self.monthly_investment = monthly_investment
    
    def simulate(self, n_sim=1000):
        months = self.years * 12
        final_wealth = []
        for _ in range(n_sim):
            wealth = 0
            for _ in range(months):
                rtn = np.random.choice(self.monthly_returns)
                wealth = wealth * (1 + rtn) + self.monthly_investment
            final_wealth.append(wealth)
        return np.array(final_wealth)

    def summary(self, final_wealth):
        mean = np.mean(final_wealth)
        p10 = np.percentile(final_wealth, 10)
        p90 = np.percentile(final_wealth, 90)
        return mean, p10, p90
