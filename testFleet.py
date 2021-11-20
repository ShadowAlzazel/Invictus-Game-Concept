#fleet tester
from levelGames import *

from collections import deque
from collections.abc import Set, Mapping
from numbers import Number


#getSize function code from https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/080_python_slots/slots.py
def getSize(obj_0):
    """Recursively iterate to sum size of object & members."""
    ZERO_DEPTH_BASES = (str, bytes, Number, range, bytearray)
    _seen_ids = set()

    def inner(obj):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, ZERO_DEPTH_BASES):
            pass  # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, 'items'):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, 'items')())
        # Check for custom object instances - may subclass above too
        if hasattr(obj, '__dict__'):
            size += inner(vars(obj))
        if hasattr(obj, '__slots__'):  # can have __slots__ with __dict__
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        return size

    return inner(obj_0)


fleet1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][1], 'ASC')
fleet2 = spaceFleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
level1 = level(14, 10, 0 ,(fleet1, fleet2), [40, 104])

print('Size of Level:', getSize(level1))