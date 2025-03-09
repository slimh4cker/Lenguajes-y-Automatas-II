grammar Invoice;

invoice 
  : header verb+ purchaseList DOT? EOF
  ;

// El nombre puede ser completo 
header 
  : NOMBRE (NOMBRE)*
  ;

// cualquier texto antes de un número es valido
verb 
  : WORD (COMMA | Y_CONJ | DE)?
  ;

// acepta 1 o más compras,separadas por ',' u 'o'
purchaseList 
  : purchase (separator purchase)*
  ;

// Los espacios despues de las comas no son obligatorios
separator : (COMMA | Y_CONJ) WS*;


// depende si se comprará piña o no (Dentro de MyVisitor solo la piña puede medirse por kilo)
purchase 
  : quantity ( unit  DE? fruit)    // Para kg
  | quantity ( pieceUnit  DE?  fruit) // Para piezas
  ;

// la cantidad puede ser por kilo o fracción, en un futuro agregar la cantidad por decimal (capaz lo pide Xenia)
quantity 
  : fraction
  | NUMBER
  ;

fraction 
  : NUMBER '/' NUMBER
  ;

unit 
  : KG
  ;

// se puede especificar la pieza por singular o plural
pieceUnit 
  : PIEZA | PIEZAS
  ;

// Las frutas se filtrarán en MyVisitor con listas y mapeo
fruit 
  : WORD
  ;


Y_CONJ : 'y';
COMMA  : ',';
KG     : 'kg';
PIEZA  : 'pieza';
PIEZAS : 'piezas';
DE     : 'de';
NUMBER : [0-9]+;
NOMBRE : [A-ZÁÉÍÓÚ][a-záéíóúñÑ]+;
WORD   : [a-zA-ZáéíóúÁÉÍÓÚñÑ]+;
DOT    : '.';
WS     : [ \t\r\n]+ -> skip;