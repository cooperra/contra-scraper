#!/bin/sh
cd "`dirname "${0}"`"
antlr4 -long-messages -Dlanguage=Python3 -o antlr_gen YAMLLexer.g4 YAMLParser.g4
