# 🌾 KrishiMitra AI WhatsApp Chatbot 🤖

### *Your AI-powered "Farmer's Friend" for hyperlocal agricultural intelligence, delivered directly through WhatsApp.*

---

## 🧠 Overview

**KrishiMitra** is a sophisticated, multilingual AI chatbot designed to empower farmers in India by providing **instant, actionable agricultural intelligence**.
It acts as a **knowledgeable companion**, helping with crop protection, financial decisions, and daily planning — all through a **simple WhatsApp interface**.

---

## ✨ Core Features

This isn't just a chatbot — it's a **suite of powerful AI tools** tailored for the modern farmer.

### 1. 🐛 Hybrid AI Pest & Disease Diagnosis

The **core innovation** of KrishiMitra.
When a user sends a photo of a sick plant, the system performs a **two-step hybrid analysis**:

* **Step 1 (Custom Model):**
  A fast, **TensorFlow/Keras-based custom model** provides an instant diagnosis in milliseconds — handling common cases efficiently.
* **Step 2 (AI Fallback):**
  If model confidence is low, the image is automatically sent to **Google Gemini Vision AI** for advanced analysis.

✅ *This hybrid architecture combines speed, accuracy, and cost-efficiency.*

---

### 2. 📈 Real-Time Market Prices (Mandi Bhav)

Ask natural-language questions like:

> “What is the price of wheat in Khargone?”

KrishiMitra fetches **up-to-the-minute mandi prices**, powered by **Gemini AI** and live market data interpretation.

---

### 3. 🌤 Hyperlocal Weather Forecasts

Get **real-time weather reports** for any city or village — including:

* Temperature
* Humidity
* Practical farming advisories

Helping farmers **plan daily agricultural activities** more effectively.

---

### 4. 🌐 Multilingual Conversational AI

KrishiMitra **understands and replies** in the user’s **native language** (e.g., Hindi, English).
Its friendly *“Krishi Mitra”* persona ensures a tone that’s always **helpful, empathetic, and clear**.

---

## ⚙️ Technology Stack & Architecture

Built on a **robust, scalable, and modern AI stack** for real-world use.

| Component                | Technology                            |
| ------------------------ | ------------------------------------- |
| **Backend Framework**    | FastAPI                               |
| **Custom ML Model**      | TensorFlow & Keras                    |
| **AI Language & Vision** | Google Gemini Pro & Gemini Pro Vision |
| **Messaging Platform**   | Twilio WhatsApp API                   |
| **Weather Data Source**  | OpenWeatherMap API                    |
| **Deployment**           | Docker + Hugging Face Spaces          |
| **Server Management**    | Gunicorn with Uvicorn workers         |

---

## 🏗 Architectural Design

KrishiMitra’s **AI Processor** acts as the central *“brain”*, intelligently routing user intent to specialized agents:

* 🐛 **Pest Detection Agent**
* 📈 **Market Price Agent**
* 🌤 **Weather Agent**

The **hybrid pest diagnosis pipeline** ensures:

* ⚡ Fast predictions for common cases (custom model)
* 🧠 Deep analysis for complex cases (Gemini Vision fallback)
* 💸 Cost-efficiency by using the paid API only when necessary

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have:

* Python **3.11+**
* A **Twilio WhatsApp Sandbox** account
* API keys for:

  * Google Gemini
  * OpenWeatherMap
  * Twilio

---

### 2. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd <your-repo-folder>

# Install dependencies
pip install -r requirements.txt
```

---

### 3. Configuration

Create a `.env` file in the project root and add your API keys:

```bash
GEMINI_API_KEY="your_gemini_api_key_here"
TWILIO_ACCOUNT_SID="your_twilio_account_sid_here"
TWILIO_AUTH_TOKEN="your_twilio_auth_token_here"
WEATHER_API_KEY="your_openweathermap_api_key_here"
```

---

### 4. Run the Application Locally

Start the FastAPI server with **Uvicorn**:

```bash
uvicorn main:app --reload
```

---

## 💬 Example Interaction (on WhatsApp)

**User:** “मक्का में कौनसी बीमारी है?”

**Bot:** “लगता है आपकी पत्ती में फंगल संक्रमण है। कृपया कॉपर-आधारित फफूंदनाशी का उपयोग करें।”

**User:** “What’s the price of soybean in Indore?”

**Bot:** “Soybean prices in Indore — ₹4500–₹5200 per quintal.”

---

## 👨‍💻 Author & Team

**Project Lead & Primary Developer**

**Shivam Rathod** — AI Engineer | Data Scientist | ML Developer

🌐 [Portfolio](https://portfolioshivamrathod.vercel.app/)
💼 [LinkedIn](https://www.linkedin.com/in/shivamrathod021)
🐙 [GitHub](https://github.com/shivamr021)
✉️ [Email](mailto:shivamrathod011@gmail.com)

---

### 🤝 Team KrishiKrew

| Name                 | Role / Contribution                                        | LinkedIn      | GitHub      |
| -------------------- | ---------------------------------------------------------- | ------------- | ----------- |
| **Shatakshi Tiwari** | Research, Ideation & Presentation Design (PPT Development) | [LinkedIn](https://www.linkedin.com/in/shatakshitiwari017/) | [GitHub](https://github.com/Shatakshi0216) |
| **Nitika Jain**           | Research & Visual Design Support (PPT & Documentation)     | [LinkedIn](https://www.linkedin.com/in/nitika-jain-b8690b353/) | [GitHub](https://github.com/nitikajain25) |
| **Sahil Kukreja**    | Frontend Developer & System Design Support                 | [LinkedIn](https://www.linkedin.com/in/sahil-kukreja-943993289/) | [GitHub](https://github.com/Sahilkukreja30) |

> 💡 *This project is submitted to the **OpenAI × NxtWave Buildathon** under team name **KrishiKrew**, featuring collaborative contributions across research, design, and AI integration.*
