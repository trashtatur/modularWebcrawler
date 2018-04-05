from spiders.StarterAbstract import Starter
from spiders.RegisteredModules import REGISTERED_MODULES, register_module


@register_module
class Run(Starter):

    def start(self):
        #this is just to test stuff
        print("OWL")
