lexer grammar TSVLexer ;
// default mode
EOL : [\r\n]+ ;
HASH :'#' -> pushMode(HASH_M), skip ;

FIELD : ( ~[# \t\r\n]+ ~[\t\r\n]* ~[ \t\r\n]+ 
        | ~[# \t\r\n] 
        | '' ) -> pushMode(FIELD_M); //TODO fix epsilon?

mode FIELD_M;
fragment WS : [ ]+ ;
SEP : WS* '\t' WS* ;
EOL4 : EOL -> type(EOL), popMode ;

FIELD2 : ( ~[ \t\r\n]+ ~[\t\r\n]* ~[ \t\r\n]+ 
         | ~[ \t\r\n] 
         | '' ) -> type(FIELD) ; //TODO fix epsilon?

mode HASH_M;

// TODO revise such that there is no error for "#<yaddaydadda foo..."
HASHCOMMENT : ( ~[<\r\n] ~[\r\n]* EOL |  EOL ) -> popMode, skip ;
LT : '<' -> pushMode(PAIR_M) ;

mode PAIR_M ;
GT : '>' -> pushMode(VALUE_M) ;
ID : [a-zA-Z_]+ ;
EOL2 : EOL -> popMode, popMode, type(EOL) ;


mode VALUE_M;
WS2 : [ \t]+ -> type(SEP), skip;
VALUE : ~[ \t\r\n]+ ~[\r\n]* ;
EOL3 : EOL -> popMode, popMode, popMode, type(EOL) ;