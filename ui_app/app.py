# import streamlit as st
# import sys
# import os
# import pandas as pd
# import yfinance as yf
# import numpy as np

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from ml_models.risk_profiling import RiskProfiler
# from ml_models.asset_clustering import AssetClusterer
# from optimization.portfolio_optimizer import PortfolioOptimizer
# from simulation.monte_carlo import MonteCarloSimulator
# from utils.investment_calculator import calculate_expected_wealth

# st.title("Goal-Based Investment Portfolio Recommender")

# goal = st.text_input("Enter your financial goal:")
# amount = st.number_input("Enter monthly amount to invest (₹):", min_value=1000)
# duration_years = st.slider("Investment duration (years):", 1, 30, 5)
# age = st.number_input("Enter your age:", min_value=18, max_value=100, value=30)
# income = st.number_input("Enter your monthly income (₹):", min_value=1000)
# investment_experience = st.number_input("Years of investment experience:", min_value=0, max_value=50)

# risk_profiler = RiskProfiler()

# if st.button("Submit"):
#     predicted_risk = risk_profiler.predict(age, income, investment_experience)
#     st.write(f"Goal: {goal}")
#     st.write(f"Monthly Investment Amount: ₹{amount}")
#     st.write(f"Duration: {duration_years} years")
#     st.write(f"Predicted Risk Level by ML Model: {predicted_risk}")

#     tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
#     prices = yf.download(tickers, start="2020-01-01", end="2025-01-01", auto_adjust=True)['Close']
#     returns = prices.pct_change().dropna()

#     clusterer = AssetClusterer(returns)
#     asset_clusters = clusterer.get_all_clusters()
#     st.header("Asset Clustering")
#     st.table(pd.DataFrame(asset_clusters, columns=['Ticker', 'Risk Category']))

#     optimizer = PortfolioOptimizer(prices)
#     portfolio_weights, (exp_return, exp_vol, sharpe) = optimizer.optimize(predicted_risk)
#     st.header("Portfolio Suggestion")
#     st.write(f"Annual Return: {exp_return:.2%}")
#     st.write(f"Volatility: {exp_vol:.2%}")
#     st.write(f"Sharpe: {sharpe:.2f}")
#     st.table(pd.DataFrame({'Weight': portfolio_weights}).sort_values('Weight', ascending=False))

#     weighted_returns = returns.dot(np.array([portfolio_weights[t] for t in tickers]))
#     monthly_returns = (1 + weighted_returns) ** (1/12) - 1  # Convert to monthly returns
#     sim = MonteCarloSimulator(monthly_returns.values, duration_years, amount)
#     final_wealth = sim.simulate()
#     mean, p10, p90 = sim.summary(final_wealth)
#     st.header("Monte Carlo Simulation")
#     st.write(f"Expected Wealth (Simulated): ₹{mean:,.2f} | 10th Percentile: ₹{p10:,.2f} | 90th Percentile: ₹{p90:,.2f}")
#     st.bar_chart(final_wealth)

#     expected_wealth_calc = calculate_expected_wealth(
#         investment_amount=amount,
#         annual_return=exp_return,
#         years=duration_years,
#         monthly_investment=True,
#     )
#     st.write(f"Expected Wealth (Calculated): ₹{expected_wealth_calc:,.2f}")
import streamlit as st

st.title("Goal Based Portfolio App")
st.success("App is working 🎉")
st.write("Now deployment is successful ✅")
