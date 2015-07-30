parser grammar TSVParser ;

options { tokenVocab=TSVLexer; }

r : (pair|row)* EOF ;

pair : LT ID GT VALUE EOL ;

row : FIELD (SEP FIELD)* EOL ;