# core/router.py

from agents import market_price_agent, weather_agent

# This file is now a simple collection of tools that can be called.
# The routing logic has been moved to the AI prompt.

def get_market_price(query: str, location: str = 'Khargone') -> str:
    """Tool to get market price."""
    return market_price_agent.get_market_price(query, location)

def get_weather_forecast(location: str) -> str:
    """Tool to get weather forecast."""
    return weather_agent.get_weather_forecast(location)