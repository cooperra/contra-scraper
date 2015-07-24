from antlr4.Lexer import TokenSource

class TokenFilter(TokenSource):

    def __init__(self, source:TokenSource):
        super().__init__()
        self._source = source
        # copy attributes
        self._factory = source._factory

    def nextToken(self):
        """Override this method."""
        return self._source.nextToken()

    def getLine(self):
        return self._source.nextToken()

    def getCharPositionInLine():
        return self._source.getCharPositionInLine()

    def getInputStream():
        return self._source.getInputStream()

    def getSourceName():
        return self._source.getSourceName()

    def setTokenFactory():
        return self._source.setTokenFactory()

    def getTokenFactory():
        return self._source.getTokenFactory()
