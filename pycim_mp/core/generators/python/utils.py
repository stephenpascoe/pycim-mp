"""Encapsualtes a set of python specific name conversion operations.

"""
# Module imports.
from operator import add

from pycim_mp.core.generators.generator_utils import *


# Module exports.
# TODO


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


# Language name constant.
LANGUAGE = 'python'

# Language prefix constant.
LANGUAGE_PREFIX = 'py'

# Language file extension constant.
FILE_EXTENSION = '.py'

# Python package initialisation file name.
_PACKAGE_INIT_FILE = '__init__'

# Python clas property field prefix.
_PROPERTY_FIELD_PREFIX = 'self.__'

# Set of simple type mappings.
_SIMPLE_TYPE_MAPPINGS = {
    'bool' : 'bool',
    'date' : 'datetime.date',
    'datetime' : 'datetime.datetime',
    'float' : 'float',
    'int' : 'int',
    'str' : 'str',
    'uri' : 'str',
    'uuid' : 'uuid.UUID',
}

# Primitive type null value.
_SIMPLE_NULL_VALUE = 'None'

# Set of simple type default values.
_SIMPLE_DEFAULT_VALUES = {
    'bool' : 'bool()',
    'datetime.date' : 'datetime.date(1900, 1, 1)',
    'datetime.datetime' : 'datetime.datetime.now()',
    'float' : 'float()',
    'int' : 'int()',
    'str' : 'str()',
    'uri' : 'str()',
    'uuid.UUID' : 'uuid.uuid4()',
}

# Iterative type default value.
_ITERATIVE_DEFAULT_VALUE = '[]'

# Iterative type null value.
_ITERATIVE_NULL_VALUE = '[]'

# Complex type default value.
_COMPLEX_DEFAULT_VALUE = '{0}()'

# Complex type null value.
_COMPLEX_NULL_VALUE = 'None'


def _strip(name):
    """Returns stripped name.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name
    return name


def _strip_class_name(name):
    """Returns stripped class name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[len(name.split('.')) - 1]
    return name


def get_ontology_name(name):
    """Converts name to a python ontology name.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name

    return name.lower()


def get_ontology_version(name):
    """Converts version identifier to a python ontology version.

    Keyword Arguments:
    name - name of version identifier being converted.

    """
    if isinstance(name, str) == False:
        name = name.version

    return name.replace(".", "_")


def get_ontology_directory(ontology, root_dir=None, sub_dir=None, suffix_root_dir=False):
    """Returns ontology directory into which code is generated code.

    Keyword Arguments:
    ontology - ontology being processed.
    root_dir - root directory with which ontology is associated.
    sub_dir - sub directory to append as a suffix.
    suffix_root_dir - flag indicating whether to append a standard suffix to root directory.

    """
    dir = ''
    if root_dir is not None:
        dir += root_dir + '/'
    if suffix_root_dir == True:
        dir += 'cim_codegen/python/'
        dir += get_ontology_name(ontology)
    dir += '/v' + get_ontology_version(ontology)
    if sub_dir is not None:
        dir += '/' + sub_dir
    return dir


def get_package_name(name):
    """Converts name to a python package name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip_package_name(name)
    return name


def get_package_path(ontology, parent, package):
    """Returns full python package name.

    Keyword Arguments:
    name - name being converted.

    """
    result = get_ontology_name(ontology)
    result += '.v'
    result += get_ontology_version(ontology)
    result += '.'
    result += get_package_name(parent)
    result += '.'
    result += get_package_name(package)
    return result


def get_package_directory(package, root_dir=None, sub_dir=None, suffix_root_dir=False):
    """Returns package directory into which code is generated code.

    Keyword Arguments:
    package - package being processed.
    root_dir - root directory with which package is associated.
    sub_dir - sub directory.
    suffix_root_dir - flag indicating whether to append a standard suffix to root directory.

    """
    dir = get_ontology_directory(package.ontology, root_dir, sub_dir, suffix_root_dir)
    dir += '/'
    dir += get_package_name(package)
    return dir


def get_class_name(name):
    """Converts name to a python class name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip_class_name(name)
    return convert_to_camel_case(name)


def get_class_import_name(name):
    """Converts name to a python class import name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip_class_name(name)
    return name


def get_class_functional_name(name):
    """Converts name to one suitable for use in a python function definition.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip_class_name(name)
    return name


def get_class_decoder_function_name(name):
    """Converts name to a python class decoder function name.

    Keyword Arguments:
    name - name being converted.

    """
    name = get_class_functional_name(name)
    return 'decode_{0}'.format(name)


def get_class_doc_string_name(name):
    """Converts name to one suitable for use in python documentation.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip_class_name(name)
    return name.replace('_', ' ')


def get_class_file_name(name):
    """Converts name to a python class file name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip_class_name(name)
    return name + FILE_EXTENSION


def get_class_base_name(name):
    """Converts name to a python base class name.

    Keyword Arguments:
    name - name being converted.

    """
    if name is not None:
        return get_class_name(name)
    else:
        return 'object'


def get_property_name(name):
    """Converts name to a python class property name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip(name)
    return name


def get_property_field_name(name):
    """Converts name to a python class property field name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip(name)
    return _PROPERTY_FIELD_PREFIX + name


def _get_default_value(type_name, is_simple, is_iterative, is_required):
    """Returns default type value.

    """
    # Iterables: convert via pre-defined mappings.
    if is_iterative:
        if is_required:
            return _get_iterative_default_value()
        else:
            return _get_iterative_null_value()
    # Simple types: convert via pre-defined mappings.
    elif is_simple:
        if is_required:
            return _get_simple_default_value(type_name)
        else:
            return _get_simple_null_value()
    # Complex types: convert via pre-defined mappings.
    else:
        if is_required:
            return _get_complex_default_value(type_name)
        else:
            return _get_complex_null_value()


def get_property_default_value(property):
    """Returns property default value.

    """
    type_name = get_type_name(property.type)
    return _get_default_value(type_name, property.type.is_simple, property.is_iterative, property.is_required)


def get_type_name(type):
    """Returns python type name.

    Keyword Arguments:
    type - a type declaration.

    """
    name = type.name
    if type.is_simple:
        return _get_simple_type_mapping(name)
    elif type.is_enum:
        return _get_simple_type_mapping('str')
    elif type.is_complex:
        return get_class_name(name)


def get_type_functional_name(type):
    """Returns python type functional name.

    Keyword Arguments:
    type - a type declaration.

    """
    name = type.name
    if type.is_simple:
        return name
    elif type.is_enum:
        return 'str'
    elif type.is_complex:
        return get_class_name(name)


def get_type_doc_name(type):
    """Returns python type documentation name.

    Keyword Arguments:
    type - a type declaration.

    """
    name = type.name
    if type.is_simple:
        return _get_simple_type_mapping(name)
    elif type.is_enum:
        return '{0}.{1}'.format(get_package_name(name), get_enum_name(name))
    elif type.is_complex:
        return '{0}.{1}'.format(get_package_name(name), get_class_name(name))


def _strip_enum_name(name):
    """Returns stripped enum name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[len(name.split('.')) - 1]
    return name


def get_enum_name(name):
    """Converts name to a python enum name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip_enum_name(name)
    return convert_to_camel_case(name)


def _get_simple_type_mapping(simple):
    """Returns matching simple type mapping.

    Keyword Arguments:
    simple - simple type name.

    """
    return _SIMPLE_TYPE_MAPPINGS[simple]


def _get_simple_default_value(simple):
    """Returns default value of a simple type.

    Keyword Arguments:
    simple - simple type name.

    """
    return _SIMPLE_DEFAULT_VALUES[simple]


def _get_simple_null_value():
    """Returns null value of a simple type.

    """
    return _SIMPLE_NULL_VALUE


def _get_iterative_default_value():
    """Returns default value of an iterative type.

    """
    return _ITERATIVE_DEFAULT_VALUE


def _get_iterative_null_value():
    """Returns null value of an iterative type.

    """
    return _ITERATIVE_NULL_VALUE


def _get_complex_default_value(complex):
    """Returns default value of a complex type.

    Keyword Arguments:
    complex - complex type name.

    """
    return _COMPLEX_DEFAULT_VALUE.format(complex)


def _get_complex_null_value():
    """Returns null value of a complex type.

    """
    return _COMPLEX_NULL_VALUE


def _strip_package_name(name):
    """Returns stripped package name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[0]
    return name


def get_package_init_file_name():
    """Returns python package init file name.

    Keyword Arguments:
    name - name being converted.

    """
    return _PACKAGE_INIT_FILE + FILE_EXTENSION


def get_package_decoder_file_name(name):
    """Converts name to a python package decoder file name.

    Keyword Arguments:
    name - name being converted.

    """
    name = get_package_name(name)
    return 'decoder_for_{0}_package'.format(name)


def get_package_imports(package):
    """Returns set of package imports.

    Keyword Arguments:
    package - package being processed.

    """
    lr = emit_line_return()
    imports = []
    o_name = get_ontology_name(package.ontology)
    o_version = get_ontology_version(package.ontology)
    p_name = get_package_name(package)
    
    def append_import(imp):
        if imp not in imports:
            imports.append(imp)

    # Set package class imports.
    for cls in package.classes:
        imp = 'from py{0}.v{1}.types.{2}.{3} import {4}'.format(
            o_name,
            o_version,
            p_name,
            get_class_import_name(cls),
            get_class_name(cls))
        append_import(imp)

    # Set type decoding imports.
    for type in [t for t in package.external_types if t.is_class]:
        imp = 'from py{0}.v{1}.decoding.{2} import {3}'.format(
            o_name,
            o_version,
            get_package_decoder_file_name(type.name_of_package),
            get_class_decoder_function_name(type))
        append_import(imp)

    if len(imports) > 0:
        return reduce(add, map(lambda i : i + lr, sorted(imports)))
    else:
        return ''


def get_package_exports(package):
    """Returns set of package exports.

    Keyword Arguments:
    package - package being processed.

    """    
    fns = []
    for cls in package.classes:
        fn = get_class_decoder_function_name(cls)
        if fn not in fns:
            fns.append(fn)

    exports = ''
    for fn in fns:
        if len(exports) > 0:
            exports += ', ' + emit_line_return() + emit_indent()
        exports += '\"{0}\"'.format(fn)

    return exports

