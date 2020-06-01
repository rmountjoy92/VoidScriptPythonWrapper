from voidscript_wrapper.utils import make_request
import os


class VoidscriptWrapper:
    def __init__(self):
        os.environ["VOIDSCRIPT_EMAIL"] = "ross.mountjoy@gmail.com"
        os.environ[
            "VOIDSCRIPT_API_KEY"
        ] = "5a13cbefa340a87f93beee5c4d3479e748d27cea4c9866b7"

    def get_version(self):
        return make_request("version", "GET")

    def register_user(self, email, password):
        return make_request(
            "register_user", "POST", payload={"email": email, "password": password}
        )

    def get_api_key(self, email, password):
        return make_request(
            "get_api_key", "POST", payload={"email": email, "password": password}
        )

    def create_character(self, user_id, name, character_class):
        return make_request(
            "create_character",
            "POST",
            payload={
                "user_id": user_id,
                "name": name,
                "character_class": character_class,
            },
        )
