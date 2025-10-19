# agents/market_price_agent.py
import google.generativeai as genai
from core.config import settings

# Configure the model at the agent level for this specific task
try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-flash-latest')
except Exception as e:
    model = None
    print(f"CRITICAL ERROR in market_price_agent: Failed to configure Gemini AI. Error: {e}")

def get_market_price(commodity: str, location: str = 'Khargone') -> str:
    """
    Gets the market price for a commodity by asking the Gemini LLM,
    requesting a WhatsApp-formatted response.
    """
    if not model:
        return "Sorry, the market price service is currently unavailable."

    if not commodity:
        return "Please specify which crop you'd like the price for."

    # --- REVISED PROMPT TO REQUEST FORMATTING ---
    prompt = (
        f"What is the most recent modal price for '{commodity}' in the '{location}' district of Madhya Pradesh, India? "
        f"Answer concisely. The final output MUST be formatted for WhatsApp using asterisks for bolding and newlines. "
        f"For example: "
        f"🌾 *Latest Price for {commodity.capitalize()}*\n\n"
        f"*- Location:* {location.capitalize()}\n"
        f"*- Price:* Around ₹[Price] per Quintal"
    )

    try:
        response = model.generate_content(prompt)
        if response.text and len(response.text) > 10:
             return response.text.strip()
        else:
             # Formatted fallback response
             return f"⚠️ Sorry, I couldn't find a specific price for *{commodity}* in *{location}* right now."

    except Exception as e:
        print(f"Market Price AI Error: {e}")
        return "Sorry, I'm having trouble connecting to the market price service right now."