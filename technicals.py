import streamlit as st

st.set_page_config(page_title="Personal Finance Chatbot", layout="centered")

st.title("💰 Personal Finance Chatbot")
st.write("Ask me about savings, taxes, or investments!")

# Simulated financial advice functions
def savings_advice(income, expenses):
    try:
        income = float(income)
        expenses = float(expenses)
        savings = income - expenses
        rate = (savings / income) * 100 if income > 0 else 0
        return f"You are saving {savings:.2f} per month, which is {rate:.1f}% of your income."
    except:
        return "Please enter valid numbers for income and expenses."

def tax_advice(income):
    try:
        income = float(income)
        if income <= 250000:
            return "You are exempt from income tax in most regions."
        elif income <= 500000:
            return "You may fall in the 5% tax bracket."
        elif income <= 1000000:
            return "You may fall in the 20% tax bracket."
        else:
            return "You may fall in the 30% tax bracket. Consider tax-saving investments under Section 80C."
    except:
        return "Enter a valid income amount."

def investment_advice(goal, duration):
    try:
        duration = int(duration)
        if goal.lower() in ["retirement", "wealth"]:
            return f"For {goal} over {duration} years, consider equity mutual funds or index funds."
        elif goal.lower() in ["short term", "emergency"]:
            return f"For {goal} over {duration} years, consider liquid funds or high-interest savings accounts."
        else:
            return "Specify a clearer goal like retirement, wealth, or emergency fund."
    except:
        return "Please enter a valid duration in years."

# Input: Basic chatbot interface
user_input = st.text_input("💬 Enter your question")

if user_input:
    user_input = user_input.lower()

    if "save" in user_input or "savings" in user_input:
        st.subheader("📊 Savings Assistant")
        income = st.text_input("Monthly Income", "50000")
        expenses = st.text_input("Monthly Expenses", "30000")
        if st.button("Calculate Savings"):
            result = savings_advice(income, expenses)
            st.success(result)

    elif "tax" in user_input or "income tax" in user_input:
        st.subheader("🧾 Tax Advisor")
        income = st.text_input("Annual Income", "600000")
        if st.button("Get Tax Advice"):
            result = tax_advice(income)
            st.success(result)

    elif "invest" in user_input or "investment" in user_input:
        st.subheader("📈 Investment Planner")
        goal = st.text_input("Investment Goal (e.g. retirement, short term, emergency)", "retirement")
        duration = st.text_input("Investment Duration (in years)", "10")
        if st.button("Get Investment Advice"):
            result = investment_advice(goal, duration)
            st.success(result)

    else:
        st.warning("❓ I can help with savings, taxes, and investments. Please ask something relevant.")
