lexer grammar DanceList_MedLex ;
// default mode
EOL : [\r\n]+ ;
ID : [a-zA-Z_]+ ;
COLON : ': ' -> pushMode(VALUE_M) ;
LONECOLON : ':' ;
IND : '  ' ;
DASH : '-' ;
EVDASH : '- ' -> pushMode(VALUE_M) ;

HASH : '#' ;

mode VALUE_M;

VALUE : ~[\r\n]+ ;
EOL2 : EOL -> popMode, type(EOL) ;
