grammar Words;

// Captura el texto
texto: (seccion_mes | otro)+ EOF;

// Captura nuevo mes
seccion_mes: MONTH COLON NEWLINE (fruta | otro)+;

// Identificar frutas
fruta: FRUIT_SINGULAR | FRUIT_PLURAL;

// Capturar otro contenido 
otro: (WORD | PUNCTUATION | WHITESPACE | NEWLINE)+;

// Definición de tokens
MONTH: 'Enero' | 'Febrero' | 'Marzo' | 'Abril' | 'Mayo' | 'Junio' | 'Julio' | 'Agosto' | 'Septiembre' | 'Octubre' | 'Noviembre' | 'Diciembre';
COLON: ':';
FRUIT_SINGULAR: 'Naranja' | 'Mandarina' | 'Toronja' | 'Fresa' | 'Guayaba' |
 'Limón' | 'Piña' | 'Mango' | 'Papaya' | 'Melón' | 'Sandía' | 'Ciruela' | 'Durazno' |
  'Higo' | 'Pera' | 'Tuna' | 'Manzana' | 'Uva' | 'Granada';
FRUIT_PLURAL: 'Naranjas' | 'Mandarinas' | 'Toronjas' | 'Fresas' | 'Guayabas' |
 'Limones' | 'Piñas' | 'Mangos' | 'Papayas' | 'Melones' | 'Sandías' | 'Ciruelas' | 'Duraznos' |
  'Higos' | 'Peras' | 'Tunas' | 'Manzanas' | 'Uvas' | 'Granadas';
WORD: [a-zA-ZáéíóúñÁÉÍÓÚÑ]+;
NUMBER: [0-9]+;
PUNCTUATION: [.,;!?¡¿];
WHITESPACE: [ \t]+;
NEWLINE: '\r'? '\n' | '\r';

// espacios en blanco ignorados
WS: [ \t\r\n]+ -> skip;