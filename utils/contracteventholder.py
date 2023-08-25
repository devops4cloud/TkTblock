import streamlit as st
from web3 import Web3

class ContractEventHolder:
    def __init__(self, contract_address: str, contract_abi: dict, w3: Web3):
        self.w3 = w3
        self.functions = contract_abi
        self.contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    def safeTransferFrom(self, fromaddress, to, id, amount, data):
        function = self.contract.functions.safeTransferFrom
        return function(fromaddress, to, id, amount, bytes(data,encoding='utf-8')).transact()

    def safeTransferFrom_form(self):
        with st.form(key="safeTransferFrom_form"):
            fromaddress =  st.selectbox("from",self.w3.eth.accounts)
            to =  st.selectbox("to",self.w3.eth.accounts)
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
            account =  st.selectbox("account",self.w3.eth.accounts)
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

    def redeemTicket(self, id, amount, account):
        function = self.contract.functions.redeemTicket
        return function(id, amount, account).transact()

    def redeemTicket_form(self):
        with st.form(key="redeemTicket_form"):
            id = st.number_input("id",min_value=0)
            amount = st.number_input("amount",min_value=0)
            account =  st.selectbox("account",self.w3.eth.accounts)
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.redeemTicket(id, amount, account)
                st.write(result)

    def getEventTicketSold(self, _id):
        function = self.contract.functions.getEventTicketSold
        return function(_id).call()

    def getEventTicketSold_form(self):
        with st.form(key="getEventTicketSold_form"):
            _id = st.number_input("_id",min_value=0)
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.getEventTicketSold(_id)
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

