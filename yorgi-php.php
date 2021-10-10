<?php
//Ecuaciones de segundo grado por formula general
//          ax 2 + bx + c = 0

//Ejemplo:  3x2 - 2x + 4 = 0

function formulaGeneral($a, $b, $c){
    $valor = ($b ** 2) - (4 * $a * $c);
    $dividendo = 2 * $a;
    $bNegativo = -$b;
    
    $x1 = "";
    if($valor < 0){
        $x1 = "(${bNegativo} + sqrt(${valor})) / ${dividendo}";
        $x2 = "(${bNegativo} - sqrt(${valor})) / ${dividendo}";
    }else {
        $x1= ( $bNegativo + sqrt($valor)) / $dividendo;
        $x2 = ($bNegativo - sqrt($valor)) / $dividendo;
    }

    return "X1 = ".$x1. " y X2 = ".$x2;
}

echo formulaGeneral(1,2,-8);



