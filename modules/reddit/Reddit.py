from modules.RegisteredModules import REGISTERED_MODULES, register_module
from modules.StarterAbstract import Starter

@register_module
class Reddit(Starter):
    def start(self):
        print("KANTALOPE")
