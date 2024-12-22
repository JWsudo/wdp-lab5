import math, keyword

print([funkcja for funkcja in dir(math) if callable(getattr(math, funkcja))])
print([funkcja for funkcja in dir(tuple) if callable(getattr(tuple, funkcja))])
print([funkcja for funkcja in dir(keyword) if callable(getattr(keyword, funkcja))])
