parser grammar DanceList_Med ;

options { tokenVocab=DanceList_MedLex; }

r : 
pair // Title
pair // Editor
pair // HomeURL
pair // BaseURL
ID LONECOLON EOL event*
HASH EOL
ID LONECOLON EOL dance*
EOF
;

pair : ID COLON VALUE? EOL
;

event : IND eventData
;

dance :
IND DASH EOL
IND IND pair // Lo
IND IND pair // Ti
IND IND pair // Au
IND IND pair // Fo
IND IND ID LONECOLON EOL event2*
;

event2 : IND IND IND eventData
;

eventData : EVDASH VALUE EOL
          ;