parser grammar DanceList_Med ;

options { tokenVocab=DanceList_MedLex; }

r : obj EOF
         ;

obj : pair+
            ;

pair : ID COLON value
          ;

value : EOL INDENT obj DEDENT // object
           | EOL INDENT listItem* DEDENT // list
           | VALUE? EOL // string or none
           ;

listItem : DASH value
              ;
