class Storage:
    def store_new_refresh_token_refresh_token(self, new_refresh_token) -> str:
        token_file = open("refresh_token", "w")
        token_file.write(new_refresh_token)
        token_file.close()

    def retrieve_refresh_token(self) -> str:
        token_file = open("refresh_token", "r")
        current_refresh_token = token_file.read()
        token_file.close()
        return current_refresh_token
