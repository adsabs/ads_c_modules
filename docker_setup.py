"""
Installer for the ADS C modules.
"""

import os
import sys
import re
sys.path.append('/proj/ads/soft/python/lib/site-packages')
#from setuptools import setup, Extension
from distutils.core import setup
from distutils.extension import Extension
import distutils.util
#from ads.ads_c_modules.utils import get_platform_specific_module

def get_platform_specific_module():
    """
    Returns the plaform specific module name for an ADS module, e.g. for the
    module Looker on a Linux platform with Python 2.4, the module name returned
    is:
    ads_c_modules_linux_x86_64_python_2_4
    """
    platform = _format_module_name(distutils.util.get_platform())
    python_version = _format_module_name(sys.version[:3])
    return 'ads_c_modules_%s_python_%s' % (platform, python_version)

def _format_module_name(name):
    """
    Returns a string with all the non-supported characters in Python module
    names.
    """
    return re.sub('\W+', '_', name)

MODULES = ['Looker', 'ctrigram', 'ldw']

PLATFORM_DIR = 'ads_c_modules/' + get_platform_specific_module()

if len(sys.argv) > 1 and sys.argv[1] == 'install':
   print "Installing in ../ads/" + PLATFORM_DIR
   if not os.path.exists('../ads/'+PLATFORM_DIR):
       os.makedirs('../ads/'+PLATFORM_DIR)
   if not os.path.exists('../ads/'+PLATFORM_DIR+'/__init__.py'):
       os.system('touch ../ads/'+PLATFORM_DIR+'/__init__.py')

EXTENSIONS = [Extension(name=mod, sources=[mod + 'module.c'])
        for mod in MODULES]

setup (
     name         = "ads_modules",
     version      = "2.3",
     description  = "Looker and other modules for ADS system",
     author       = "Markus Demleitmer, Edwin Henneken",
     author_email = "ads@cfa.harvard.edu",
     url          = "http://adsabs.harvard.edu",
     extra_path   = '/proj/ads/soft/adspy/' + PLATFORM_DIR,
     ext_modules  = EXTENSIONS,
)
