from contracts.validator import ResponseValidator

class BrsapValidator(ResponseValidator):

    def validate(self, data):
        return data