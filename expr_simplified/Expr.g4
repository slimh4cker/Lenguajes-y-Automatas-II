grammar Expr;

expr: term expr_prime;
expr_prime: /* ε */
            | ADD term expr_prime
            | SUBTRACT term expr_prime;

term: factor term_prime;
term_prime: /* ε */
            | MULTI factor term_prime
            | DIVI factor term_prime;

factor: ID
        | LEFT_PARENTH expr RIGHT_PARENTH;


ADD: '+';
SUBTRACT: '-';
MULTI: '*';
DIVI: '/';
LEFT_PARENTH: '(';
RIGHT_PARENTH: ')';
ID: DIGIT+;
DIGIT: [0-9];
WS: [ \t\r\n]+ -> skip;
