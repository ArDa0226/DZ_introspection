
def introspection_info(obj):

    object_type = type(obj)

    attribute = dir(obj)
    attribute_1 = [method for method in attribute if not callable(getattr(obj, method))]

    methods = [method for method in attribute if callable(getattr(obj, method))]

    module = obj.__class__.__module__

    information = {'type': object_type,
                   'attribute': attribute_1,
                   'methods': methods,
                   'module': module}

    return information

number_information = introspection_info(23)
print(number_information)

str_information = introspection_info('Привет')
print(str_information)

list_information = introspection_info([2, 34, 4.5, 'Hello'])
print(list_information)


