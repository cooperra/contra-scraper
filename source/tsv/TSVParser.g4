parser grammar TSVParser ;

options { tokenVocab=TSVLexer; }

r : (pair|row)* EOF ;

pair : HASHKEY SEP VALUE EOL ;

row : FIELD (SEP FIELD)* EOL ;