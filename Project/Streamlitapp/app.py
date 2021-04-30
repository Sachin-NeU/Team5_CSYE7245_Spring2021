import streamlit as st
from multiapp import MultiApp
from apps import home, stock_details,twitter,model # import your app modules here
# HomePage styling

st.write('')
st.markdown(
    """
<style>
.css-1l02zno {
    background-color:#2596be;
    background-attachment: fixed;
    flex-shrink: 0;
    height: 100vh;
    color:black;
    overflow: auto;
    padding: 5rem 1rem;
    position: relative;
    transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
    width: 21rem;
    z-index: 100;
    margin-left: 0px;
}
.css-145kmo2 {
    font-size: 1rem;
    color: white;
    margin-bottom: 0.4rem;
}
.css-1vbb94r {
    width: 100%;
    margin-bottom: 1rem;
    border-collapse: collapse;
    border-radius: 30px;
    background-color: white;
    font-weight: bold;
}
.css-hi6a2p {
    flex: 1 1 0%;
    width: 100%;
    padding: 3rem 1rem 10rem;
    max-width: 730px;
}
canvas{
    width:800px !important;
    height:420px !important;
}
.css-1wrcr25 {
    display: flex;
    flex-direction: row;
    -webkit-box-pack: start;
    place-content: flex-start;
    -webkit-box-align: stretch;
    align-items: stretch;
    position: absolute;
    inset: 0px;
    overflow: hidden;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}body{background-color: lightgreen;
    font-family: "Times New Roman", Times, serif}
</style>
""",
    unsafe_allow_html=True,
)

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Stocks Data", stock_details.app)
app.add_app("Twitter Data", twitter.app)
app.add_app("Prediction", model.app)
# The main app
app.run()