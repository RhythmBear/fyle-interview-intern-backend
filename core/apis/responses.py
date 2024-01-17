from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data, status_code=200):
        # Added option to pass status code into the respond function.
        return make_response(jsonify(data=data), status_code)
