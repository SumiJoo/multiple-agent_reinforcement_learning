import importlib
import os.path as osp
# the author of the article used imp module, but it is too old
# so I changed to importlib

def load(name):
    pathname = osp.join(osp.dirname(__file__), name)
   
    spec = importlib.util.spec_from_file_location(None, pathname)
   
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module