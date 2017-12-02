def django_view_function(request, x):
    return x


class DjangoViewClass(object):
    def __init__(self):
        pass

    @classmethod
    def as_view(cls):
        def view_function(request, x):
            return x
        return view_function


# in practice, this would be called in a Django URLconf file
view = DjangoViewClass.as_view()
