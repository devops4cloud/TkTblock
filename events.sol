// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC1155/extensions/ERC1155Supply.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/finance/PaymentSplitter.sol";

contract TkTBlock is ERC1155, Ownable, ERC1155Supply, Pausable, PaymentSplitter{

    constructor(
        address[] memory _payees,
        uint256[] memory _shares 
    )
    ERC1155("https://ipfs.io/ipfs/bafybeidlf22wc73c75gdqnl26wvjzhykwglx5djiyjdgqplclrnxxlbk3m/")
    PaymentSplitter(_payees, _shares)
    {}

    // Create a struct to hold the event information
    struct Event {
        uint128 _event_Id;
        string _eventName;
        string _eventDate; 
        string _eventVenue;
        uint128 _eventTicketPrice;
        uint128 _eventTicketSupply;
        string _eventURL;
        uint128 _eventTicketSold;
        address _eventHolder;
    }

    // Create a mapping of events with the identifiers
    mapping(uint => Event) public events;


    // Create a function to add a new event

    function addEvent(uint128 _id, string memory _eventName, string memory _eventDate, string memory _eventVenue, uint128 _eventTicketPrice, uint128 _eventTicketSupply,string memory _eventURL, uint128 _eventTicketSold, address _eventHolder) public {
            events[_id] = Event(_id, _eventName, _eventDate, _eventVenue, _eventTicketPrice, _eventTicketSupply, _eventURL, _eventTicketSold, _eventHolder);

    }
    // Create a function to get details about the event
    function getEventDetails(uint128 _id) external view returns (uint, string  memory, string memory, string memory, uint128, uint128,string memory, uint128, address) {
            Event storage _event = events[_id];
            return (_event._event_Id,_event._eventName,_event._eventDate, _event._eventVenue, _event._eventTicketPrice, _event._eventTicketSupply, _event._eventURL, _event._eventTicketSold, _event._eventHolder);
    }

    // Create a function to get event id
    function getEventId(uint128 _id) public view returns (uint128){
        Event memory _eventa = events[_id];
        return _eventa._event_Id;

    }
    // Create a function to get event holder
    function getEventHolder(uint128 _id) public view returns (address){
       Event memory _eventa = events[_id];
       return _eventa._eventHolder;
    }

    // Create a function to get the ticket price
    function getEventTicketPrice(uint128 _id) public view returns (uint128){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketPrice;

    }
    // Create a function to get the ticket supply
    function getEventTicketSupply(uint128 _id) public view returns (uint128){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketSupply;

    }
    // Create a function to get the amount of tickets sold 
    function getEventTicketSold(uint128 _id) public view returns (uint128){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketSold;

    }
    // Create a function to update the number of tickets sold 
    function updateEventTicketSold(uint128 _id, uint128 amount) public {
        Event storage _eventa = events[_id];
        _eventa._eventTicketSold += amount;
    }

    // Creating the buy tickets function
    function buyTickets(uint128 id, uint128 amount)
        public
        payable
    {
        //Verifying the event ID is valid and the amount passed is correct.
        require(getEventId(id) > 0, "Event ID is not valid");

        //Checking to see whether there are enough tickets available for sale
        require(getEventTicketSold(id) + amount <= getEventTicketSupply(id), "Amount exeeds total supply or event sold out" );

        // Checking the amount transfered is enough to purchase the ticket
        require(msg.value == amount * getEventTicketPrice(id), "Not enough funds sent or too much funds sent");

        //Minting the tickets
        _mint(msg.sender, id, amount, "");

        // Update the tickets sold variable for the event
        updateEventTicketSold(id, amount);
    }

    //Adding the URI function to customize the URL to match the token for OpenSea compatibility
    function uri(uint128 _id) public view virtual returns (string memory) {
            require (exists(_id), "URI Token does not exist");
            return string(abi.encodePacked(super.uri(_id),Strings.toString(_id),".json"));
    }

    function contractURI() public pure returns (string memory){
            return "https://ipfs.io/ipfs/bafybeidlf22wc73c75gdqnl26wvjzhykwglx5djiyjdgqplclrnxxlbk3m/collection.json";

    }
    // Ability for the owner to distribute tickets a.k.a airdrop
    function airdropTickets(uint128 _id, address[] calldata recipients, uint128 amount) external onlyOwner {
            for (uint128 i =0; i < recipients.length; i++){
                _safeTransferFrom(msg.sender, recipients[i], _id, amount,"");
            }
    }
    // Function to redeem Tickets by Event Holders
    function redeemTicket(uint128 id, uint128 amount, address account) public {
        require(getEventId(id) > 0, "Event ID is not valid");
        require(msg.sender == getEventHolder(id), "You are not authorized to redeem tickets for this event" );
        require(balanceOf(account, id) >= amount, "Insufficient balance or you don't own tickets");
        
        _burn(account, id, amount);
    }
    function _beforeTokenTransfer(address operator, address from, address to, uint256[] memory ids, uint256[] memory amounts, bytes memory data)
        internal
        whenNotPaused
        override(ERC1155, ERC1155Supply)
    {
        super._beforeTokenTransfer(operator, from, to, ids, amounts, data);
    }

    function setURI(string memory newuri) public onlyOwner {
        _setURI(newuri);
    }

}