import streamlit as st
from web3 import Web3

class ContractCustomer:
    def __init__(self, contract_address: str, contract_abi: dict, w3: Web3):
        self.w3 = w3
        self.functions = contract_abi
        self.contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    def buyTickets(self, id, amount):
        function = self.contract.functions.buyTickets
        return function(id, amount).call()

    def buyTickets_form(self):
        with st.form(key="buyTickets_form"):
            id = st.number_input("id",min_value=0)
            amount = st.number_input("amount",min_value=0)
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.buyTickets(id, amount)
                st.write(result)

    def safeTransferFrom(self, fromaddress, to, id, amount, data):
        function = self.contract.functions.safeTransferFrom
        return function(fromaddress, to, id, amount, data).call()

    def safeTransferFrom_form(self):
        with st.form(key="safeTransferFrom_form"):
            fromaddress = st.text_input("from")
            to = st.text_input("to")
            id = st.number_input("id",min_value=0)
            amount = st.number_input("amount",min_value=0)
            data = st.text_input("data")
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.safeTransferFrom(fromaddress, to, id, amount, data)
                st.write(result)

    def balanceOf(self, account, id):
        function = self.contract.functions.balanceOf
        return function(account, id).call()

    def balanceOf_form(self):
        with st.form(key="balanceOf_form"):
            account = st.text_input("account")
            id = st.number_input("id",min_value=0)
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.balanceOf(account, id)
                st.write(result)

    def getEventDetails(self, _id):
        function = self.contract.functions.getEventDetails
        return function(_id).call()

    def getEventDetails_form(self):
        with st.form(key="getEventDetails_form"):
            _id = st.number_input("_id",min_value=0)
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.getEventDetails(_id)
                st.write(result)

def dynamic_inputs(input_name):
    container = st.container()

    input_values = []

    if st.button('Add input'):
        input_values.append(container.text_input(input_name, key=len(input_values)))

    with st.form(key='submit_form'):
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.write(f'Submitted values: {input_values}')

