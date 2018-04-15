try:
    value = None
except ImportError:
    value = 1
    value = 2
except AttributeError:
    value = 3
except:
    value = 4
