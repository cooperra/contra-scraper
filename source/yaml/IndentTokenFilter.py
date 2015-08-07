from .TokenFilter import TokenFilter

class IndentTokenFilter(TokenFilter):
    def __init__(self, source, lexer=None):
        super().__init__(source)
        self._reset()
        if lexer is None:
            lexer = source
        self.EOF = -1 # Token.EOF
        self.EOL = lexer.EOL
        self.IND = lexer.IND
        self.INDENT = lexer.INDENT
        self.DEDENT = lexer.DEDENT

    def reset(self):
        super().reset()
        self._reset()

    def _reset(self):
        self.indents = [0]
        self.newLineFlag = True
        """True when we're at the start of a line for the first time"""
        self.eofFound = False
        """True once we've delt with the special case of EOF"""
        self.tokenQueue = []
        """Push to front, pop from back"""

    def popToken(self):
        if len(self.tokenQueue) == 0:
            return super().nextToken()
        else:
            return self.tokenQueue.pop()

    def pushToken(self, token):
        self.tokenQueue.insert(0, token)

    def nextToken(self):
        token = self.popToken()
        if token.type == self.EOF and not self.eofFound:
            self.eofFound = True
            if not self.newLineFlag:
                # inject EOL to force dedent (also helps match parser rules)
                eolToken = token.clone()
                eolToken.type = self.EOL
                self.pushToken(eolToken)
            # put EOF back in the queue
            self.pushToken(token)
        elif token.type == self.EOL:
            self.newLineFlag = True
            return token
        elif self.newLineFlag:
            self.newLineFlag = False
            # newLineFlag means that it's time to manage indents
            # or that it's safe to emit an EOF
            currentInd = 0
            firstToken = token
            while token.type == self.IND:
                  currentInd += 1
                  token = self.popToken()
            if token.type == self.EOL:
                # ignore this entire line because it is only whitespace
                self.newLineFlag = True
            else:
                # eof indent special case
                if token.type == self.EOF:
                    # next token is EOF
                    # ignore indents and dedent to zero regardless
                    currentInd = 0
                
                # deal with indents
                if self.indents[-1] == currentInd:
                    # no change
                    # deal with non-indent token later
                    self.pushToken(token)
                elif self.indents[-1] < currentInd:
                    # indent
                    # push indent token
                    indentToken = firstToken.clone()
                    indentToken.type = self.INDENT
                    indentToken.text = "<INDENT>"
                    indentToken.start = -1
                    indentToken.stop = -1
                    self.pushToken(indentToken)
                    self.indents.append(currentInd)
                    # push non-indent token
                    self.pushToken(token)
                elif self.indents[-1] > currentInd:
                    # dedent
                    dedentToken = firstToken.clone()
                    dedentToken.type = self.DEDENT
                    dedentToken.text = "<DEDENT>"
                    dedentToken.start = -1
                    dedentToken.stop = -1
                    while self.indents[-1] > currentInd:
                        self.indents.pop()
                        # push dedents
                        self.pushToken(dedentToken)
                    if self.indents[-1] < currentInd:
                        # dedented too far somehow
                        raise Exception("Unlikely!")
                    # push normal token
                    self.pushToken(token)
                else:
                    raise Exception("Impossible: exaustive elifs")
        else:
            # normal token
            # treat normally
            return token
        # recurse until we get a normal token
        return self.nextToken()
                
                
            
