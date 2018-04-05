from spiders.RegisteredModules import REGISTERED_MODULES


def build_all_modules():
    for module in REGISTERED_MODULES:
        module_created = module()
        module_created.start()


build_all_modules()
