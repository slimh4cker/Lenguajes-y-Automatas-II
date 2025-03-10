grammar Words;

// Captura el texto
texto: (seccion_mes | otro)+ EOF;

// Captura un nuevo mes
seccion_mes: MONTH COLON WHITESPACE* otro+;

// Capturar otro contenido 
otro: (WORD | PUNCTUATION | COLON | WHITESPACE | NEWLINE | NUMBER)+;

// Definición de tokens
MONTH: 'Enero' | 'Febrero' | 'Marzo' | 'Abril' | 'Mayo' | 'Junio' | 'Julio' | 'Agosto' | 'Septiembre' | 'Octubre' | 'Noviembre' | 'Diciembre';
COLON: ':';
WORD: [a-zA-ZáéíóúñÁÉÍÓÚÑ]+;
PUNCTUATION: [-—.,;!?¡¿];
NUMBER: [0-9]+;
WHITESPACE: [ \t]+;
NEWLINE: ('\r'? '\n' | '\r');
