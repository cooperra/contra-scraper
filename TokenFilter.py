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
