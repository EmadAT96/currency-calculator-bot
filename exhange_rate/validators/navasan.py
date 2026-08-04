from contracts.validator import ResponseValidator

class NavasanValidator(ResponseValidator):

    def validate(self, data):
        return data