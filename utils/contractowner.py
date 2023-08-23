import streamlit as st
from web3 import Web3
from datetime import date

class ContractOwner:
    def __init__(self, contract_address: str, contract_abi: dict, w3: Web3):
        self.w3 = w3
        self.functions = contract_abi
        self.contract = w3.eth.contract(address=contract_address, abi=contract_abi)
        print(w3.is_connected())

    def addEvent(self, _id, _eventName, _eventDate, _eventVenue, _eventTicketPrice, _eventTicketSupply, _eventURL, _eventTicketSold, _eventHolder):
        function = self.contract.functions.addEvent
        return function(_id, _eventName, _eventDate, _eventVenue, _eventTicketPrice, _eventTicketSupply, _eventURL, _eventTicketSold, _eventHolder).call()

    def addEvent_form(self):
        with st.form(key="addEvent_form"):
            _id = st.number_input("_id",min_value=0)
            _eventName = st.text_input("_eventName")
            _eventDate = st.date_input("_eventDate",min_value=date.today())
            _eventVenue = st.text_input("_eventVenue")
            _eventTicketPrice = st.number_input("_eventTicketPrice",min_value=0)
            _eventTicketSupply = st.number_input("_eventTicketSupply",min_value=0)
            _eventURL = st.text_input("_eventURL")
            _eventTicketSold = st.number_input("_eventTicketSold",min_value=0)
            _eventHolder = st.text_input("_eventHolder")
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.addEvent(_id, _eventName, _eventDate, _eventVenue, _eventTicketPrice, _eventTicketSupply, _eventURL, _eventTicketSold, _eventHolder)
                st.write(result)

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

    def getEventTicketPrice(self, _id):
        function = self.contract.functions.getEventTicketPrice
        return function(_id).call()

    def getEventTicketPrice_form(self):
        with st.form(key="getEventTicketPrice_form"):
            _id = st.number_input("_id",min_value=0)
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.getEventTicketPrice(_id)
                st.write(result)

    def airdropTickets(self, _id, recipients, amount):
        function = self.contract.functions.airdropTickets
        return function(_id, recipients, amount).call()

    def airdropTickets_form(self):
        with st.form(key="airdropTickets_form"):
            _id = st.number_input("_id",min_value=0)
            recipients = st.text_input("recipients")
            amount = st.number_input("amount",min_value=0)
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.airdropTickets(_id, [recipients], [amount])
                st.write(result)

    def getEventTicketSupply(self, _id):
        function = self.contract.functions.getEventTicketSupply
        return function(_id).call()

    def getEventTicketSupply_form(self):
        with st.form(key="getEventTicketSupply_form"):
            _id = st.number_input("_id",min_value=0)
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.getEventTicketSupply(_id)
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

    def release(self, account):
        function = self.contract.functions.release
        return function(account).call()

    def release_form(self):
        with st.form(key="release_form"):
            account = st.text_input("account")
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.release(account)
                st.write(result)

    def safeBatchTransferFrom(self, fromaddress, to, ids, amounts, data):
        function = self.contract.functions.safeBatchTransferFrom
        return function(fromaddress, to, ids, amounts, data).call()

    def safeBatchTransferFrom_form(self):
        with st.form(key="safeBatchTransferFrom_form"):
            fromaddresss = st.text_input("from")
            to = st.text_input("to")
            ids = st.number_input("ids",min_value=0)
            amounts = st.number_input("amounts",min_value=0)
            data = st.text_input("data")
            submit_button = st.form_submit_button(label="Call")

            if submit_button:
                result = self.safeBatchTransferFrom(fromaddresss, to, [ids], [amounts], [data])
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

