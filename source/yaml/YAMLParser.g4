parser grammar YAMLParser ;

options { tokenVocab=YAMLLexer; }

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
