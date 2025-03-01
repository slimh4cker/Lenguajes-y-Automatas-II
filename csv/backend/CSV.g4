grammar CSV;

file: header row+ EOF;

header: non_empty_row;

non_empty_row: field (COMMA field)* NEWLINE;

row: (field (COMMA field)*)? NEWLINE;

field: TEXT?;

TEXT: ~[,\r\n]+;

COMMA: ',';
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;