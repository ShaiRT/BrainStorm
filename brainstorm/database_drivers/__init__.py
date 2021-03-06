"""A package for database drivers to be used by brainstorm.saver

Any DriverNameDriver class in a '.py' file in this directory
will be included in the package.
Files starting with '_' will be ignored.
The package imports as a dictionary of {'driver_name': DriverNameDriver}.

The drivers should inplement the interface for the brainstorm.saver
"""
import importlib
import inspect
import stringcase as sc
import sys

from pathlib import Path


drivers = dict()
root = Path(inspect.getsourcefile(lambda: 0)).absolute().parent
for path in root.glob('**/*.py'):
    if path.name.startswith('_'):
        continue
    sys.path.insert(0, str(path.parent))
    m = importlib.import_module(path.stem,
                                package='brainstorm.database_drivers')
    sys.path.pop(0)
    for name, obj in m.__dict__.items():
        if inspect.isclass(obj):
            if not name.endswith('Driver'):
                continue
            driver_name = sc.snakecase(name)[:-7]
            drivers[driver_name] = obj

sys.modules[__name__] = drivers
