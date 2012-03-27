"""Generates code to represent an ontology as a set of types.

"""

# Module imports.
from pycim_mp.core.cim_exception import CIMException
from pycim_mp.core.generators.base_generator import BaseGenerator
from pycim_mp.core.generators.generator_utils import *
from pycim_mp.core.generators.python.utils import *


# Module exports.
__all__ = ['TypesGenerator']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


# Generator key.
_GEN_KEY = 'types'

# Generator language identifier.
_GEN_LANG = 'python'



def _get_template(filename):
    """Helper function to return templates.

    """
    return get_template(filename, _GEN_LANG, _GEN_KEY)



class TypesGenerator(BaseGenerator):
    """Generates code to represent an ontology as a set of types.

    """
    def __init__(self, ontology, opts):
        """Constructor.

        Keyword Arguments:
        ontology - to be parsed during course of code generation.
        opts - code generation options.

        """
        # Constructor chaining.
        super(TypesGenerator, self).__init__(ontology, opts)


    def on_ontology_parse(self, ont):
        """Event handlers for the ontology parse event.

        Keyword Arguments:
        ont - ontology being processed.

        """
        super(TypesGenerator, self).on_ontology_parse(ont)
        
        # Helper functions.
        def emit_imports():
            return self.__emit_imports_for_root_package()
        def emit_exports():
            return self.__emit_exports_for_root_package()

        # Create package directory.
        dir = get_ontology_directory(ont, self.opts.out_dir, 'types', self.opts.out_suffix)
        create_directory(dir)

        # Create package init file.
        code = self.__emit_package_init_file('types_root_package.txt',
                                             emit_imports,
                                             emit_exports)
        file = dir + '/' + get_package_init_file_name()
        write_file(code, file)


    def on_package_parse(self, pkg):
        """Event handlers for the package parse event.

        Keyword Arguments:
        pkg - package being processed.

        """
        super(TypesGenerator, self).on_package_parse(pkg)

        # Helper functions.
        def emit_imports():
            return self.__emit_imports_for_sub_package(pkg)
        def emit_exports():
            return self.__emit_exports_for_sub_package(pkg)

        # Create package directory.
        dir = get_package_directory(pkg, self.opts.out_dir, 'types', self.opts.out_suffix)
        create_directory(dir)

        # Create package init file.
        code = self.__emit_package_init_file('types_sub_package.txt',
                                             emit_imports,
                                             emit_exports)

        file = dir + '/' + get_package_init_file_name()
        write_file(code, file)


    def on_class_parse(self, cls):
        """Event handlers for the class parse event.

        """
        super(TypesGenerator, self).on_class_parse(cls)

        pkg = cls.package
        code = self.__emit_class(pkg, cls)
        dir = get_package_directory(pkg, self.opts.out_dir, 'types', self.opts.out_suffix)
        file = dir + '/' + get_class_file_name(cls)
        write_file(code, file)


    def on_enum_parse(self, enum):
        """Event handlers for the enum parse event.

        """
        super(TypesGenerator, self).on_enum_parse(enum)

        pkg = enum.package
        code = self.__emit_enum(pkg, enum)
        dir = get_package_directory(pkg, self.opts.out_dir, 'types', self.opts.out_suffix)
        file = dir + '/' + enum.name + '.py'
        write_file(code, file)


    def __emit_package_init_file(self, template, package_imports_fn, package_exports_fn):
        """Emits a package initialisation file.

        Keyword Arguments:
        template - code template to use.
        package_imports_fn - function for creating set of package imports.
        package_exports_fn - function for creating set of package exports.

        """
        # Open template.
        code = _get_template(template)

        # Set helper vars.
        module_imports = package_imports_fn()
        module_exports = package_exports_fn()

        # Generate code.
        code = inject_standard_template_params(self.ontology, self.opts, code)
        code = code.replace('{module-imports}', module_imports)
        code = code.replace('{module-exports}', module_exports)

        return code


    def __emit_imports_for_root_package(self):
        """Emits code corresponding to a set of root package imports.

        """
        code = ''
        for pkg in self.ontology.packages:
            code += self.__emit_imports_for_sub_package(pkg)
        return code


    def __emit_imports_for_sub_package(self, pkg):
        """Emits code corresponding to a set of sub package imports.

        Keyword Arguments:
        pkg - package being parsed.

        """
        lr = emit_line_return()

        code = ''
        for cls in pkg.classes:
            code += 'from py{0}.v{1}.types.{2}.{3} import {4}{5}'.format(
                get_ontology_name(self.ontology),
                get_ontology_version(self.ontology),
                get_package_name(pkg),
                get_class_import_name(cls),
                get_class_name(cls),
                lr)
        return code


    def __emit_exports_for_root_package(self):
        """Emits code corresponding to a set of root package exports.

        """
        code = ''
        emit_comma = False

        for pkg in self.ontology.packages:
            if len(pkg.classes) > 0:
                if emit_comma:
                    code += ', '
                code += self.__emit_exports_for_sub_package(pkg)
                emit_comma = True

        return code


    def __emit_exports_for_sub_package(self, pkg):
        """Emits code corresponding to a set of sub package exports.

        Keyword Arguments:
        pkg - package being parsed.

        """
        emit_comma = False

        code = ''
        for cls in pkg.classes:
            if emit_comma:
                code += ', '
            code += '\'{0}\''.format(get_class_name(cls))
            emit_comma = True
        return code


    def __emit_class(self, pkg, cls):
        """Emits code corresponding to a python class.

        Keyword Arguments:
        pkg - package being parsed.
        cls - class being parsed.

        """
        # Set helper vars.
        class_ctor = self.__emit_class_ctor(pkg, cls)
        class_imports = self.__emit_class_imports(cls.imports)
        class_circular_imports = self.__emit_class_imports(cls.circular_imports)
        class_properties = self.__emit_properties(pkg, cls)
        class_representations = self.__emit_class_representations(pkg, cls)

        # Open template.
        if cls.is_abstract:
            code = _get_template('class_abstract.txt')
        else:
            code = _get_template('class.txt')

        # Generate code.        
        code = inject_standard_template_params(self.ontology, self.opts, code)
        code = code.replace('{package-name}', get_package_name(pkg))
        code = code.replace('{class-name}', get_class_name(cls))
        code = code.replace('{base-class-name}', get_class_base_name(cls.base))
        code = code.replace('{class-doc-string}', cls.doc_string)
        code = code.replace('{class-imports}', class_imports)
        code = code.replace('{class-circular-imports}', class_circular_imports)
        code = code.replace('{class-ctor}', class_ctor)
        code = code.replace('{class-properties}', class_properties)
        code = code.replace('{class-representations}', class_representations)

        return code


    def __emit_enum(self, pkg, enum):
        """Emits code corresponding to a python class.

        Keyword Arguments:
        pkg - package being parsed.
        enum - enum being parsed.

        """
        # Open template.
        code = _get_template('enum.txt')

        # Generate code.
        code = inject_standard_template_params(self.ontology, self.opts, code)
        code = code.replace('{enum-name}', get_enum_name(enum))
        code = code.replace('{enum-doc-string}', enum.doc_string)

        return code


    def __emit_class_ctor(self, pkg, cls):
        """Emits code corresponding to a python class constructor.

        Keyword Arguments:
        pkg - package being parsed.
        cls - class being parsed.

        """
        code = ''
        tmp = ''

        # Initialise property fields.
        for prp in cls.properties:
            tmp = '{0} = {1}'.format(
                get_property_field_name(prp),
                get_property_default_value(prp),
            )
            #print tmp
            code += '{0}{1}{2}# type = {3}{4}'.format(
                emit_indent(2),
                tmp,
                ''.ljust(60 - len(tmp)),
                get_type_doc_name(prp.type),
                emit_line_return(),
            )            

        if code == '':
            code = '{0}pass'.format(emit_indent(2))
        code += emit_line_return()

        return code


    def __emit_class_imports(self, imports):
        """Emits code corresponding to a set of python class imports.

        Keyword Arguments:
        imports - imports being parsed.

        """
        from pycim_mp.core.ontology.class_info import ClassInfo
        from pycim_mp.core.ontology.package_info import PackageInfo

        code = ''

        for package, type in imports:
            pkg_path = get_package_path(self.ontology, 'types', package)
            type_name = get_class_name(type)
            type_import_name = get_class_import_name(type)
            code += 'from py{0}.{1} import {2}'.format(pkg_path, type_import_name, type_name)
            code += emit_line_return()

        return code


    def __emit_properties(self, pkg, cls):
        """Emits code corresponding to a set of python class properties.

        Keyword Arguments:
        pkg - package being parsed.
        cls - class being parsed.

        """
        code = ''

        for prp in cls.properties:
            code += self.__emit_property(pkg, cls, prp)

        return code


    def __emit_property(self, pkg, cls, prp):
        """Emits code corresponding to a python class property.

        Keyword Arguments:
        pkg - package being parsed.
        cls - class being parsed.
        prp - class property being parsed.

        """
        # Set helper vars.
        doc_string = prp.doc_string
        if len(doc_string) > 1:
            doc_string = emit_line_return(2) + emit_indent(2) + doc_string

        # Open template.
        code = ''
        if prp.is_iterative:
            code = _get_template('class_property_iterative.txt')
        else:
            if prp.is_required:
                code = _get_template('class_property.txt')
            else:
                code = _get_template('class_property_nullable.txt')

        # Generate code.        
        code = code.replace('{property-name}', get_property_name(prp))
        code = code.replace('{property-field}', get_property_field_name(prp))
        code = code.replace('{property-typename}', get_type_name(prp.type))
        code = code.replace('{property-doc-string}', doc_string)
        code = code.replace('{class-doc-name}', get_class_doc_string_name(cls))
        code += emit_line_return(3)

        return code


    def __emit_class_representations(self, pkg, cls):
        """Emits code corresponding to a set of python class representations.

        Keyword Arguments:
        pkg - package being parsed.
        cls - class being parsed.

        """
        # Set dict ctor.
        dict_ctor = ''
        if cls.base is not None:
            dict_ctor = 'super({class-name}, self).as_dict()'

        # Set dict items.
        dict_items = ''
        for prp in cls.properties:
            dict_items += "{0}append(d, '{1}', {2}, {3}, {4}, {5})".format(
                emit_line_return() + emit_indent(2),
                get_property_name(prp),
                get_property_field_name(prp),
                prp.is_iterative,
                prp.type.is_simple,
                prp.type.is_enum)

        # Open template.
        code = _get_template('class_representations.txt')

        # Generate code.
        code = code.replace('{dict-ctor}', dict_ctor)
        code = code.replace('{dict-items}', dict_items)
        code = code.replace('{class-name}', get_class_name(cls))

        return code

