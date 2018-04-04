from modules.StarterAbstract import Starter
from modules.RegisteredModules import REGISTERED_MODULES, register_module


@register_module
class Run(Starter):

    def start(self):
        #this is just to test stuff
        print("OWL")
