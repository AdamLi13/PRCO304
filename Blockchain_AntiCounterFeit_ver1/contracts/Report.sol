pragma solidity ^0.6.0;


library Things{

    struct Items {
        string id; 
        string name; 
        string creator; 
        // uint256 [] timestamps;
        string ownerName; 
        string ownerRole;
        string customer; 
        address owner; 
        bool flag;
    }

    struct User{
        string name; 
        bool flag; 
    }
}

contract Reports{
    // string type manufacturer, distributor, retailer, customer;
    using Things for Things.Items;
    using Things for Things.User;
    
    mapping(string => mapping(address => Things.User)) register;
    mapping(string => Things.Items) id2item;
    mapping(address => bool) fake;

    constructor() public
    {

    }

    function blackUser(address send) public{
        fake[send] = true;
    }

    function isBlackUser(address send) public returns (bool) {
        return fake[send];
    }

    function isExist(address send, string memory role) public view returns (bool) {
        return register[role][send].flag;
    }

    function unique(string memory id) public returns (bool){
        return id2item[id].flag;
    }

    function addUser(address send, string memory name, string memory role) public returns (bool) {
        if(isExist(send, role)){
            return false;
        }
        register[role][send].name = name;
        register[role][send].flag = true;
        return true;
    }
    
    // , uint256 timestamp
    function addProduct(address send, string memory id, string memory name) public returns (bool){
        string memory role = "manufacturer";
        if(isExist(send, role) == false){
            return false;
        }

        if(unique(id)){
            return false;
        }

        Things.User memory holder = register[role][send]; 

        id2item[id].id = id; 
        id2item[id].name = name; 
        id2item[id].creator = holder.name; 
        // id2item[id].timestamps.push(timestamp); 
        id2item[id].flag = true; 
        id2item[id].ownerName = holder.name; 
        id2item[id].ownerRole = role; 
        id2item[id].owner = send; 
        return true;
    }

    // , uint256 timestamp
    function transfer(address send, string memory id, string memory role) public returns (bool){
        if(isExist(send, role) == false){
            return false;
        }
        if(unique(id) == false){
            return false;
        }
        
        Things.User memory holder = register[role][send]; 
        // id2item[id].timestamps.push(timestamp); 
        id2item[id].ownerName = holder.name; 
        id2item[id].ownerRole = role; 
        id2item[id].owner = send; 
        return true;
    }

    function getItemById(string memory id) public returns (bool, string memory, string memory, string memory, string memory, string memory){
        string memory ret = "";
        if(unique(id) == false){
            return (false, ret, ret, ret, ret, ret);
        }
        Things.Items memory item = id2item[id];
        return (true, item.id, item.name, item.creator, item.ownerName, item.ownerRole);
    }

    function checkFake(string memory id) public returns (bool){
        
        if(unique(id) == false){
            return true;
        }
        Things.Items memory item = id2item[id];
        if(isExist(item.owner, item.ownerRole) == false){
            return true;
        }
        return isBlackUser(item.owner);
    }
}
