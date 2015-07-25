lexer grammar YAMLLexer ;
// default mode
EOL : [\r\n]+ ;
ID : [a-zA-Z_]+ ;
COLON : ':' -> pushMode(VALUE_M) ;
IND : '  ' ;
DASH : '-' -> pushMode(VALUE_M) ;

HASHCOMMENT : '#' ~[\r\n]* EOL -> skip ;

mode VALUE_M;
WS : [ \t]+ -> skip ;
VALUE : ~[ \t\r\n]+ ~[\r\n]* ;
EOL2 : EOL -> popMode, type(EOL) ;

mode UNUSED;

DEDENT : IND* ;
INDENT : IND* ;