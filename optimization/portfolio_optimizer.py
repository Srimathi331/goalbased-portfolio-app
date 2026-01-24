from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import sample_cov

class PortfolioOptimizer:
    def __init__(self, prices_df):
        self.prices = prices_df

    def optimize(self, risk_level):
        mu = mean_historical_return(self.prices)
        S = sample_cov(self.prices)

        # ✅ Risk level target volatility
        target_map = {
            "Low": 0.12,
            "Medium": 0.18,
            "High": 0.25
        }

        # default
        target_vol = target_map.get(risk_level, 0.18)

        # ✅ LOW RISK
        if risk_level == "Low":
            ef = EfficientFrontier(mu, S)
            ef.min_volatility()

        # ✅ HIGH RISK
        elif risk_level == "High":
            ef = EfficientFrontier(mu, S)
            ef.max_sharpe(risk_free_rate=0.0)

        # ✅ MEDIUM RISK (safe handling)
        else:
            # 1) Find min possible volatility
            ef1 = EfficientFrontier(mu, S)
            ef1.min_volatility()
            min_vol = ef1.portfolio_performance(verbose=False)[1]

            # 2) Find max possible volatility (using max_sharpe portfolio)
            ef2 = EfficientFrontier(mu, S)
            ef2.max_sharpe(risk_free_rate=0.0)
            max_vol = ef2.portfolio_performance(verbose=False)[1]

            # 3) Clamp target inside range
            target_vol = max(min_vol, min(target_vol, max_vol))

            # 4) Optimize using safe target volatility
            ef = EfficientFrontier(mu, S)
            ef.efficient_risk(target_volatility=target_vol)

        weights = ef.clean_weights()
        return weights, ef.portfolio_performance(verbose=False)
