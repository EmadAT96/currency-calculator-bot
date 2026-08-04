class ProviderRegistry:
    _providers = {}

    @classmethod
    def register(
        cls,
        name,
        provider_class,
        mapper_class,
        validator_class
    ):
        cls._providers[name] = {
            "provider_class": provider_class,
            "mapper_class": mapper_class,
            "validator_class": validator_class
        }

    @classmethod
    def get(cls, name):

        if name not in cls._providers:
            raise ValueError(
                f"Provider {name} Not Found"
            )
        
        return cls._providers[name]

def register_provider(name, mapper_class, validator_class):

    def decorator(provider_class):
        ProviderRegistry.register(
            name,
            provider_class,
            mapper_class,
            validator_class
        )

        return provider_class

    return decorator