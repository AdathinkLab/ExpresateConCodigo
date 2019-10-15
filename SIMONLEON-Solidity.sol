pragma solidity ^0.5.0;

contract Adivina {
    address internal owner;
    uint256 internal num;
    uint256 public numGanador;
    uint256 public precio;
    bool public juego;
    address public ganador;
    uint256 public inversionInicial;
    
    constructor(uint256 _numeroGanador, uint256 _precio) public payable{
        owner = msg.sender;
        num = 0;
        numGanador = _numeroGanador;
        precio = _precio;
        juego = true;
        inversionInicial = msg.value;
    }
    
    function comprobarAcierto(uint256 _num) private view returns(bool) {
        if(_num == numGanador) {
            return true;
        } else {
            return false;
        }
    }
    function numeroRandom() private view returns(uint256) {
        return uint256( keccak256( abi.encode (now, msg.sender, num))) % 10;
    }
    function participar() external payable returns(bool resultado, uint256 numero) {
        require(juego == true);
        require(msg.value == precio);
        uint256 numUsuario = numeroRandom();
        bool acierto = comprobarAcierto(numUsuario);
        if(acierto == true) {
            juego = false;
            msg.sender.transfer(inversionInicial + (num * (precio/2)));
            ganador = msg.sender;
            resultado = true;
            numero = numUsuario;
        } else {
            num ++;
            resultado = false;
            numero = numUsuario;
        }
    }
    
    function verPremio() public view returns(uint256) {
        if(juego == true){
            return inversionInicial + (num *(precio/2));
        } else {
            return 0;
        }
    }
    
    function retirarFondosContrato() external returns(uint256) {
        require(msg.sender == owner);
        require(juego == false);
        uint256 cantidad = address(this).balance;
        msg.sender.transfer(cantidad);
        return cantidad;
    }
}