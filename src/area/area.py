class Area:

    def __init__(self, token_string):
        self.token_list = token_string.split("\n")

    def is_token(self, token):
        for x in self.token_list:
            if x == token:
                return True
        return False
