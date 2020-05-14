class Area:

    def __init__(self, token_list):
        self.token_list = []
        self.token_list = token_list

    def is_token(self, token):
        for x in self.token_list:
            if x == token:
                return True
        return False