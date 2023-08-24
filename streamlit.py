import streamlit as st
import yaml
from passlib.hash import pbkdf2_sha256
import os
from web3 import Web3
from utils.contractowner import ContractOwner
from utils.contractcustomer import ContractCustomer
from utils.contracteventholder import ContractEventHolder
import json
from dotenv import load_dotenv
from pathlib import Path

#LOAD environment variables
load_dotenv('BLOCK.env')

# Replace these values with your contract address and ABI
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
ABI_FILE = os.getenv('ABI_FILE') #"ABI.json"

with open(Path(ABI_FILE)) as f:
    info_json = json.load(f)

CONTRACT_ABI = info_json

# Replace these values with your Ethereum node URL and private key
ETHEREUM_NODE_URL = os.getenv('ETHEREUM_NODE_URL') #'HTTP://127.0.0.1:7545'
PRIVATE_KEY = os.getenv('PRIVATE_KEY')


w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))
w3.eth.default_account = w3.eth.account.from_key(PRIVATE_KEY).address

# Load user data from YAML file
def load_user_data():
    with open("config.yaml", "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader) or {}

# Save user data to YAML file
def save_user_data(data):
    with open("config.yaml", "w") as file:
        yaml.dump(data, file)

# Register a new user
def register_user(username, password, user_type):
    users = load_user_data()
    if username in users:
        st.warning("User already exists. Please choose another username.")
    else:
        hashed_password = pbkdf2_sha256.hash(password)
        users[username] = {"password": hashed_password, "user_type": user_type}
        save_user_data(users)
        st.success("Registration successful. You can now log in.")

# Authenticate a user
def authenticate_user(username, password):
    users = load_user_data()
    if username in users:
        stored_password = users[username]["password"]
        if pbkdf2_sha256.verify(password, stored_password):
            st.session_state["auth"] = True
            st.session_state["role"] =  users[username]["user_type"]
            return True
    return False

# Streamlit UI
st.title("User Authentication App")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
login_section = st.empty()  # Create an empty section for login

if menu == "Register":
    st.header("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    user_type = st.text_input("User Type")

    if st.button("Register"):
        if username and password and user_type:
            register_user(username, password, user_type)

if menu == "Login":
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.success(f"Welcome, {username}!")
            login_section.empty()  # Clear the login section
        else:
            st.error("Authentication failed. Please check your credentials.")


# Uncomment the following line to display user data for debugging purposes.
#st.write(load_user_data())

if "auth" in st.session_state and st.session_state["auth"]:
    role = st.session_state["role"]
    if role == "owner":
        contract_owner = ContractOwner(CONTRACT_ADDRESS, CONTRACT_ABI, w3)  
        st.title('Owner/Admin Section') 
        select_transaction = st.selectbox("Select transaction:"
                                        ,("Create Event", "Buy Tickets","Get Event Details","Get Event Tickets sold",
                                            "Get Event ticket price","Air Drop Tickets","Get Event Tickets Supply",
                                            "Check an account balance","Release","Ticket Transfer"))    
        if select_transaction == "Create Event":
            contract_owner.addEvent_form()
        elif select_transaction == "Buy Tickets":
            contract_owner.buyTickets_form()
        elif select_transaction == "Get Event Details":
            contract_owner.getEventDetails_form()
        elif select_transaction == "Get Event Tickets sold":
            contract_owner.getEventTicketSold_form()
        elif select_transaction == "Get Event ticket price":
            contract_owner.getEventTicketPrice_form()
        elif select_transaction == "Air Drop Tickets":
            contract_owner.airdropTickets_form()
        elif select_transaction == "Get Event Tickets Supply":
            contract_owner.getEventTicketSupply_form()
        elif select_transaction == "Check an account balance":
            contract_owner.balanceOf_form()
        elif select_transaction == "Release":
            contract_owner.release_form()
        elif select_transaction == "Ticket Transfer":
            contract_owner.safeBatchTransferFrom_form() 
    elif role == "user":
        contract_customer = ContractCustomer(CONTRACT_ADDRESS, CONTRACT_ABI, w3)
        

        st.title('Customer Section')    
        select_transaction = st.selectbox("Select transaction",("Buy Tickets","Ticket Transfer",
                                                                "Check Ticket Balance","View Event Details"))

        if select_transaction == "Buy Tickets":
            contract_customer.buyTickets_form()
        elif select_transaction == "Ticket Transfer":
            contract_customer.safeTransferFrom_form()
        elif select_transaction == "Check Ticket Balance":
            contract_customer.balanceOf_form()
        elif select_transaction == "View Event Details":
            contract_customer.getEventDetails_form()    
    elif role == "event_holder":
        contract_eventholder = ContractEventHolder(CONTRACT_ADDRESS, CONTRACT_ABI, w3)

        st.title('Event Holder Section')    
        select_transaction = st.selectbox("Select transaction",("Redeem Tickets","Ticket Transfer",
                                                                "Check Ticket Balance","View Event Details",
                                                                "Get Event Tickets Sold"))

        if select_transaction == "Redeem Tickets":
            contract_eventholder.redeemTicket_form()
        elif select_transaction == "Ticket Transfer":
            contract_eventholder.safeTransferFrom_form()
        elif select_transaction == "Check Ticket Balance":
            contract_eventholder.balanceOf_form()
        elif select_transaction == "View Event Details":
            contract_eventholder.getEventDetails_form()
        elif select_transaction == "Get Event Tickets Sold":
            contract_eventholder.getEventTicketSold_form()
    