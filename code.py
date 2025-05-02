# Tesla_Stock_analysis.py

# ------------------------------
# ✅ IMPORT LIBRARIES
# ------------------------------
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go

# ------------------------------
# ✅ SECTION 1: YFINANCE - Tesla Stock Data
# ------------------------------
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

# ------------------------------
# ✅ SECTION 2: WEB SCRAPING - Tesla Revenue Data
# ------------------------------
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

# Locate the correct table
tables = soup.find_all("table")
for table in tables:
    if "Tesla Quarterly Revenue" in table.text:
        revenue_table = table
        break

tesla_revenue = pd.read_html(str(revenue_table))[0]
tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(',|\$', '', regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

# ------------------------------
# ✅ SECTION 3: PLOT - Tesla Stock & Revenue
# ------------------------------
def make_graph(stock_data, revenue_data, stock):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name="Stock Price"))
    fig.add_trace(go.Scatter(x=revenue_data['Date'], y=revenue_data['Revenue'], name="Revenue"))
    fig.update_layout(
        title=f"{stock} Stock Price and Revenue (Up to June 2021)",
        xaxis_title="Date",
        yaxis_title="USD",
        legend_title="Metric",
        height=600,
        width=1000
    )
    fig.show()

make_graph(tesla_data, tesla_revenue, "Tesla")







#Gamestop_Stock_analysis.py

# ------------------------------
# ✅ IMPORT LIBRARIES
# ------------------------------
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go

# ------------------------------
# ✅ SECTION 1: YFINANCE - GameStop Stock Data
# ------------------------------
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)

# ------------------------------
# ✅ SECTION 2: WEB SCRAPING - GameStop Revenue Data
# ------------------------------
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url).text
soup = BeautifulSoup(html_data_2, "html.parser")

tables = pd.read_html(html_data_2)
gme_revenue = tables[1]
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(',|\$', '', regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]

# ------------------------------
# ✅ SECTION 3: PLOT - GameStop Stock & Revenue
# ------------------------------
def make_graph(stock_data, revenue_data, stock):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name="Stock Price"))
    fig.add_trace(go.Scatter(x=revenue_data['Date'], y=revenue_data['Revenue'], name="Revenue"))
    fig.update_layout(
        title=f"{stock} Stock Price and Revenue (Up to June 2021)",
        xaxis_title="Date",
        yaxis_title="USD",
        legend_title="Metric",
        height=600,
        width=1000
    )
    fig.show()

make_graph(gme_data, gme_revenue, "GameStop")

