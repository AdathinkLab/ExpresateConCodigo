<?php

/*Dada una serie de palabras separadas por espacios, escribir la frase formada 
por las mismas palabras en orden inverso. Cada palabra estará formada exclusivamente 
por letras, y existirá exactamente un espacio entre cada pareja de palabras. 
La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", 
de un espacio en blanco y de la frase invertida.

Ejemplo de entrada:
    this is a test
    foobar
    all your base

Salida correspondiente:
    Case #1: test a is this
    Case #2: foobar
    Case #3: base your all
*/

$i = 1;

function ffff (string $str) {
    global $i;

    $arr = explode(" ", $str);
    $arr_inv = array_reverse($arr);
    $cadena = implode(" ", $arr_inv);

    echo "Case #{$i}: ".$cadena."\n";
    $i++; 

    ffffx2();
}

function ffffx2 () {
    $str = readline("Ingresa tu oracion: "); 
    ffff($str);
}

ffffx2();

