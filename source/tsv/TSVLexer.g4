lexer grammar TSVLexer ;
// default mode
EOL : [\r\n]+ ;
ID : [a-zA-Z_]+ ;
fragment WS : [ ]+ ;
SEP : WS* '\t' WS* ;

// TODO revise such that there is no error for "#<yaddaydadda foo..."
HASHCOMMENT : ( HASH ~[<\r\n] ~[\r\n]* EOL
              | HASH EOL ) -> skip ;
HASH :'#' ;
HASHKEY : '<' ID '>' -> pushMode(HASHPAIR) ;

FIELD : ~[ \t\r\n]+ ~[\t\r\n]* ~[ \t\r\n]+ | ~[ \t\r\n] | '' ; //TODO fix epsilon

mode HASHPAIR;
SEP2 : SEP -> type(SEP), pushMode(VALUE_M) ;
EOL2 : EOL -> popMode, type(EOL) ;


mode VALUE_M;
VALUE : ~[ \t\r\n]+ ~[\r\n]* ;
EOL3 : EOL -> popMode, type(EOL) ;
