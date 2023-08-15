// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC1155/extensions/ERC1155Supply.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract myContract is ERC1155, Ownable, ERC1155Supply, Pausable {

    constructor()
    ERC1155("https://ipfs.io/ipfs/bafybeidlf22wc73c75gdqnl26wvjzhykwglx5djiyjdgqplclrnxxlbk3m/")
    {}

    // Create a struct to hold the event information
    struct Event {
        uint _event_Id;
        string _eventName;
        string _eventDate; 
        string _eventVenue;
        uint256 _eventTicketPrice;
        uint256 _eventTicketSupply;
        string _eventURL;
        uint256 _eventTicketSold;

    }
    // Create a mapping of events with the identifiers
    mapping(uint => Event) public events;


    // Create a function to add a new event

    function addEvent(uint _id, string memory _eventName, string memory _eventDate, string memory _eventVenue, uint256 _eventTicketPrice, uint256 _eventTicketSupply,string memory _eventURL, uint256 _eventTicketSold) public {
            events[_id] = Event(_id, _eventName, _eventDate, _eventVenue, _eventTicketPrice, _eventTicketSupply, _eventURL, _eventTicketSold);

    }

    // Create a function to get details about the event
    function getEventDetails(uint _id) external view returns (uint, string  memory, string memory, string memory, uint256, uint256,string memory, uint256) {
            Event storage _event = events[_id];
            return (_event._event_Id,_event._eventName,_event._eventDate, _event._eventVenue, _event._eventTicketPrice, _event._eventTicketSupply, _event._eventURL, _event._eventTicketSold );

    }

    // Create a function to get event id
    function getEventId(uint _id) public view returns (uint){
        Event memory _eventa = events[_id];
        return _eventa._event_Id;

    }

    // Create a function to get event name
    function getEventName(uint _id) public view returns (string memory){
        Event memory _eventa = events[_id];
        return _eventa._eventName;

    }
    // Create a function to update event name
    function updateEventName(uint _id, string memory _eName) public {
        Event storage _eventa = events[_id];
        _eventa._eventName = _eName;
    }
    // Create a function to get the ticket price
    function getEventTicketPrice(uint _id) public view returns (uint){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketPrice;

    }
    // Create a function to update the ticket price
    function updateEventTicketPrice(uint _id, uint _eventTicketPrice) public {
        Event storage _eventa = events[_id];
        _eventa._eventTicketPrice = _eventTicketPrice;
    }
    // Create a function to get the ticket supply
    function getEventTicketSupply(uint _id) public view returns (uint){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketSupply;

    }
    // Create a function to update the ticket supply
    function updateEventTicketSupply(uint _id, uint _eventTicketSupply) public {
        Event storage _eventa = events[_id];
        _eventa._eventTicketSupply = _eventTicketSupply;
    }

    // Create a function to get the amount of tickets sold 
    function getEventTicketSold(uint _id) public view returns (uint){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketSold;

    }
    // Create a function to update the number of tickets sold 
    function updateEventTicketSold(uint _id, uint amount) public {
        Event storage _eventa = events[_id];
        _eventa._eventTicketSold += amount;
    }

    // Modifying the minting to allow payments and also checking the ability to purchase the tickets.
    // Add Max Supply tracking and checking availability of tickets.
    function buyTickets(uint256 id, uint256 amount)
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
    function uri(uint256 _id) public view virtual override returns (string memory) {
            require (exists(_id), "URI Token does not exist");
            return string(abi.encodePacked(super.uri(_id),Strings.toString(_id),".json"));
    }
    //Adding a contract level URI for OpenSea compatibility
    function contractURI() public pure returns (string memory){
            return "https://ipfs.io/ipfs/bafybeidlf22wc73c75gdqnl26wvjzhykwglx5djiyjdgqplclrnxxlbk3m/collection.json";

    }

    // Ability for the owner to distribute tickets a.k.a airdrop
    function airdropTickets(uint256 _id, address[] calldata recipients, uint amount) external onlyOwner {
            for (uint i =0; i < recipients.length; i++){
                _safeTransferFrom(msg.sender, recipients[i], _id, amount,"");
            }
    }
    
    //Adding a withdrawal contract so that only the owner can transfer
    function withdraw() public onlyOwner {
        require(address(this).balance > 0, "Balance is 0");
        payable(owner()).transfer(address(this).balance);
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