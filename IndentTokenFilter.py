from TokenFilter import TokenFilter

class IndentTokenFilter(TokenFilter):
    def __init__(self, source, lexer=None):
        super().__init__(source)
        self.indents = [0]
        self.atLineStart = True
        self.tokenQueue = []
        if lexer is None:
            lexer = source
        self.EOL = lexer.EOL
        self.IND = lexer.IND
        self.DED = lexer.DED

    def popToken(self):
        if len(self.tokenQueue) == 0:
            return super().getToken()
        else:
            return self.tokenQueue.pop()

    def pushToken(self, token):
        self.tokenQueue.append(token)

    def getToken(self):
        token = self.popToken()
        if token.type == self.EOF and not self.atLineStart:
            # inject EOL to force dedent (also helps match parser rules)
            eolToken = token.clone()
            eolToken.type = self.EOL
            self.pushToken(eolToken)
            # put EOF back in the queue
            self.pushToken(token)
        elif token.type == self.EOL:
            self.atLineStart = True
            return token
        elif self.atLineStart:
            self.atLineStart = False
            currentInd = 0
            firstToken = token
            while token.type == self.IND:
                  currentInd += 1
                  token = self.popToken()
            if self.indents[-1] == currentInd:
                # no change
                # deal with non-indent token later
                self.pushToken(token)
            elif self.indents[-1] < currentInd:
                # indent
                # push indent token
                self.pushToken(firstToken)
                self.indents.append(currentInd)
                # push non-indent token
                self.pushToken(token)
            elif self.indents[-1] > currentInd:
                # dedent
                dedentToken = firstToken.clone()
                dedentToken.type = self.DED
                while self.indents[-1] > currentInd:
                    self.indents.pop()
                    # push dedents
                    self.pushToken(firstToken)
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
        return self.getToken()
                
                
            
