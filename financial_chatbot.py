import pandas as pd
import gradio as gr

df = pd.read_csv("data\\finance_data_numeric.csv")




def financial_chatbot(question):
    q = question.lower()

    # --- case 1: revenue ---
    if "revenue" in q:
        revenues = df.groupby("Company")["Total Revenue"].sum()
        response = "\n".join([f"{company}: ${int(rev):,}" for company, rev in revenues.items()])
        return "Total revenue by company (last 3 years combined):\n" + response

    # --- case 2: net income ---
    elif "net income" in q:
        incomes = df.groupby("Company")["Net Income"].sum()
        response = "\n".join([f"{company}: ${int(val):,}" for company, val in incomes.items()])
        return "Total net income by company:\n" + response

    # --- case 3: assets ---
    elif "assets" in q:
        assets = df.groupby("Company")["Total Assets"].sum()
        response = "\n".join([f"{company}: ${int(val):,}" for company, val in assets.items()])
        return "Total assets by company:\n" + response

    # --- case 4: liabilities ---
    elif "liabilities" in q:
        liabilities = df.groupby("Company")["Total Liabilities"].sum()
        response = "\n".join([f"{company}: ${int(val):,}" for company, val in liabilities.items()])
        return "Total liabilities by company:\n" + response

    # --- case 5: cash flow ---
    elif "cash flow" in q:
        cashflow = df.groupby("Company")["Cash Flow from Operating Activities"].sum()
        response = "\n".join([f"{company}: ${int(val):,}" for company, val in cashflow.items()])
        return "Cash flow from operations by company:\n" + response

    # --- fallback ---
    else:
        return f"I'm not an expert on that 😅, but I'm a financial chatbot 🤖. Try asking me about 'revenue', 'net income', 'assets', etc."



iface = gr.Interface(
    fn=financial_chatbot,
    inputs=gr.Textbox(lines=2, placeholder="Ask a financial question..."),
    outputs="text",
    title="Financial Chatbot",
    description="Ask about Total Revenue, Net Income, or Cash Flow from Operating Activities for Apple, Microsoft, and Tesla."
)

iface.launch()


