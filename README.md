# TkTblock Blockchain Digital Ticketing - Team 2 
<img src="/Images/BC.png" width="900" height="400">

---
The TKTblock application has the potential to resolve many pressing issues currently facing the event industry and offers a faster way to create traceable and transferable tickets. It also enhances security, ensures ticket validity, and provides more control over the secondary market.
With the use of blockchain technology.

# Platform Capabilities-Contract Owner 
* Setup the smart contract
* Initiates the event with details
* Setup the commission shares between the Artist, Event space, and contract Owner
* Free ticket giveaways (airdrop)
* Event changes are made
* Event promotions
  
## Platform Capabilities-Artist
* Specifies the event agenda
* Requests the commission shares
* Organizes the event
* Promotes the event
  
## Platform Capabilities-EventSpace
* Provides seating capacity
* Admits the fans Check ticket balances
* Verifies ticket authenticity
* Requests the commission shares
* Promotes the event
  
## Platform Capabilities-Customer
* Buy tickets
* Check balances
* Transfer tickets
* Check event details

## User Journey - Customer 

<img src="/Images/UJ-customer.png" width="1000" height="600">

## User Journey - holder 

<img src="/Images/UJ-eventholder.png" width="1000" height="600">

## User Journey - Event Organizer 

<img src="/Images/UJ-Event%20Organizer.png" width="3000" height="400">

## Technologies
Multiple technologies and statistical models are used to build the insider Application
- Python
- Remix
- Metamask
- Ganache
- Web3 Library
- Stremlit
- Open Zeppelin libraries
- Github

## Installation Guide

The user of the application will have to download Python,Python package manager PIP and Git.

   - [How to install Python](https://www.python.org/downloads/) 
   - [How to install PIP ](https://pip.pypa.io/en/stable/installation/) 
   - [How to install Git ](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
   - Streamlit : pip install streamlit


### Usage

- Clone repository:

```bash

$ git clone https://github.com/devops4cloud/TkTblock.git
$ cd ./TkTblock

```
- Open REMIX Studio: https://remix.ethereum.org/
   - Copy or upload events.sol
   - Compile file with solidity 0.8.0
   - Deploy to test network (Ganache is prefered)
   - Copy Contract Address
  

- Install libraries:

```bash

$ pip install streamlit
$ pip install web3
$ pip install passlib

```

- Edit .env file
   - Rename empty_BLOCK.env to BLOCK.env
   - Add the following parameters:
      - CONTRACT_ADDRESS=CONTRACT ADDRESS FROM TEST NETWORK
      - ABI_FILE=./Files/abi.json
      - ETHEREUM_NODE_URL= TEST NETWORK ADDRESS
      - PRIVATE_KEY= CONTRACT OWNER PRIVATE KEY

- Run streamlit app

```bash
$ streamlit run streamlit.py

```

## Contributors

This application is developed by [Luis](https://github.com/lumiroga), [Joe](https://github.com/EthernetWink), [Mario](https://github.com/devops4cloud), [AlGhalia](https://github.com/alghalia), [Naf](https://github.com/nafeezurc)

---

## License

Copyright: N/A
