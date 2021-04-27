import streamlit as st
from multiapp import MultiApp
from apps import home, stock_details # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Stocks", stock_details.app)

# The main app
app.run()