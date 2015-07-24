parser grammar DanceList_Med ;

options { tokenVocab=DanceList_MedLex; }

r : obj[0] EOF
         ;

obj[int ind] : pair[ind]+
            ;

pair[int ind] : varind[ind] ID COLON value[ind]
          ;

value[int ind] : EOL obj[ind+1] // object
           | EOL listItem[ind+1]* // list
           | VALUE? EOL // string or none
           ;

varind[int ind] : {$ind > 0}? IND varind[ind-1]
                | {$ind == 0}? /* epsilon */
                ;

/*countind
    returns [int i]
    : {i=0} ( IND {i+=1 } )* ;

/*countind
    returns [int i]
    : IND countind {i=1+$countind.i}
    | {i=0}
    ;
*/

listItem[int ind] : varind[ind] DASH value[ind]
              ;
