#!/bin/sh
cd "`dirname "${0}"`"
antlr4 -long-messages -Dlanguage=Python3 -o antlr_gen TSVLexer.g4 TSVParser.g4
