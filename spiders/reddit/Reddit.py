from spiders.RegisteredModules import REGISTERED_MODULES, register_module
from spiders.StarterAbstract import Starter

@register_module
class Reddit(Starter):
    def start(self):
        print("KANTALOPE")
