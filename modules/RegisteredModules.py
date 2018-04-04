REGISTERED_MODULES = []

def register_module(cls):
    REGISTERED_MODULES.append(cls)
    return cls
