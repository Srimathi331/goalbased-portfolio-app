from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import sample_cov

class PortfolioOptimizer:
    def __init__(self, prices_df):
        self.prices = prices_df

    def optimize(self, risk_level):
        mu = mean_historical_return(self.prices)
        S = sample_cov(self.prices)
        ef = EfficientFrontier(mu, S)
        if risk_level == "Low":
            ef.min_volatility()
        elif risk_level == "High":
            ef.max_sharpe()
        else:
            ef.efficient_risk(target_volatility=0.18)
        weights = ef.clean_weights()
        return weights, ef.portfolio_performance(verbose=False)
