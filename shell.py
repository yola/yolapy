import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


from yolapy.services import Yola
from tests.test_integration.test_settings import auth, url


yola = Yola(url=url, auth=auth)

print 'The current directory has been added to the beginning of sys.path'
print 'and the Yola service client has been instantiated as `yola`.'
