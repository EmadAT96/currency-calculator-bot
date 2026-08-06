from exhange_rate.contracts.validator import ResponseValidator

class ExchangeValidator(ResponseValidator):

    def validate(self, data):
        
        if data.get("success") and data.get("success") == True:
            return data
        
        error = data["error"]
        
        raise ValueError(f"{error['code']} ({error['type']}): {error['info']}")