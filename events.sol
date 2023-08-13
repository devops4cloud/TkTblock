// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC1155/extensions/ERC1155Supply.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract myContract is ERC1155, Ownable, ERC1155Supply, Pausable {

    constructor()
    ERC1155("https://bafybeidlrbnewpy5dttzmv5rvhuwd5duja4vqavty3pnwi3v3z22f5vzau.ipfs.w3s.link/")
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
    function get_eventId(uint _id) public view returns (uint){
        Event memory _eventa = events[_id];
        return _eventa._event_Id;

    }

// Create a function to get event name
    function get_eventName(uint _id) public view returns (string memory){
        Event memory _eventa = events[_id];
        return _eventa._eventName;

    }
// Create a function to update event name
    function update_eventName(uint _id, string memory _eName) public {
        Event storage _eventa = events[_id];
        _eventa._eventName = _eName;
    }
// Create a function to get the ticket price
    function get_eventTicketPrice(uint _id) public view returns (uint){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketPrice;

    }
// Create a function to update the ticket price
    function update_eventTicketPrice(uint _id, uint _eventTicketPrice) public {
        Event storage _eventa = events[_id];
        _eventa._eventTicketPrice = _eventTicketPrice;
    }
// Create a function to get the ticket supply
    function get__eventTicketSupply(uint _id) public view returns (uint){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketSupply;

    }
// Create a function to update the ticket supply
    function update__eventTicketSupply(uint _id, uint _eventTicketSupply) public {
        Event storage _eventa = events[_id];
        _eventa._eventTicketSupply = _eventTicketSupply;
    }

// Create a function to get the amount of tickets sold 
    function get__eventTicketSold(uint _id) public view returns (uint){
        Event memory _eventa = events[_id];
        return _eventa._eventTicketSold;

    }
// Create a function to update the number of tickets sold 
    function update__eventTicketSold(uint _id, uint amount) public {
        Event storage _eventa = events[_id];
        _eventa._eventTicketSold += amount;
    }

    // Modifying the minting to allow payments and also checking the ability to purchase the tickets.
    // Add Max Supply tracking and checking availability of tickets.
    function buyTickets(uint256 id, uint256 amount)
        public
        payable
    {

        //require(id <= eventTicketSupply.length, "This event does not exist"); 
        //require(id >= 0, "This event does not exit");
        require(get_eventId(id) > 0, "Event ID is not valid");
        require(get__eventTicketSold(id) + amount <= get__eventTicketSupply(id), "Amount exeeds total supply or event sold out" );
        require(msg.value == amount * get_eventTicketPrice(id), "Not enough funds sent or too much funds sent");
        _mint(msg.sender, id, amount, "");

        // Update the tickets sold variable for the event
        update__eventTicketSold(id, amount);
    }

        //Adding the URI function to customize the URL to match the token
    function uri(uint256 _id) public view virtual override returns (string memory) {
            require (exists(_id), "URI Token does not exist");
            return string(abi.encodePacked(super.uri(_id),Strings.toString(_id),".json"));
    
    }
    //Adding a withdrawal contract so that 
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
