"""Generates code to perform xml decoding.

"""

# Module imports.
from operator import add

from pycim_mp.core.generators.base_generator import BaseGenerator
from pycim_mp.core.generators.generator_utils import *
from pycim_mp.core.generators.python.utils import *

# Module exports.
__all__ = ['DecodersGenerator']


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
_GEN_KEY = 'decoders'

# Generator language identifier.
_GEN_LANG = 'python'


def _get_template(filename):
    """Helper function to return templates.

    """
    return get_template(filename, _GEN_LANG, _GEN_KEY)


class DecodersGenerator(BaseGenerator):
    """Generates code to perform xml decoding.

    """
    def __init__(self, ontology, opts):
        """Constructor.

        Keyword Arguments:
        ontology - ontology from which code is generated.
        opts - code generation options.

        """
        # Constructor chaining.
        super(DecodersGenerator, self).__init__(ontology, opts)


    def on_ontology_parse(self, ont):
        """Event handlers for the ontology parse event.

        Keyword Arguments:
        ont - ontology being processed.

        """
        super(DecodersGenerator, self).on_ontology_parse(ont)

        # Create code output directory.
        dir = get_ontology_directory(ont, self.opts.out_dir, 'decoding', self.opts.out_suffix)
        create_directory(dir)

        # Create python package init file.
        code = self.__emit_root_package_init_file()
        file = dir + '/' + get_package_init_file_name()
        write_file(code, file)


    def on_package_parse(self, pkg):
        """Event handlers for the package parse event.

        Keyword Arguments:
        pkg - package being processed.

        """
        super(DecodersGenerator, self).on_package_parse(pkg)

        id = emit_indent()
        lr = emit_line_return()

        def get_decoder_functions():
            fns = ''
            for cls in pkg.classes:
                dcs = self.__get_decodings(cls)
                fn = _get_template('decoder_function.txt')
                fn = fn.replace('{class-name}', get_class_name(cls))
                fn = fn.replace('{class-function-name}', get_class_functional_name(cls))
                fn = fn.replace('{class-doc-name}', get_class_doc_string_name(cls))
                fn = fn.replace('{class-decodings}', dcs)
                fn += emit_line_return(3)
                fns += fn
            return fns

        # Open template.
        code = _get_template('decoder.txt')

        # Generate code.
        code = inject_standard_template_params(self.ontology, self.opts, code)
        code = code.replace('{module-exports}', get_package_exports(pkg))
        code = code.replace('{module-imports}', get_package_imports(pkg))
        code = code.replace('{decoding-functions}', get_decoder_functions())

        # Create decoder.
        file = self.__get_decoder_file_name(pkg)
        write_file(code, file)


    def __get_decodings(self, cls):
        """Returns class level decodings.

        Keyword Arguments:
        cls - class being processed.

        """
        code = ''
        for p in cls.all_properties:
            for dc in cls.get_property_decodings(p):
                code += self.__emit_decoding(p, dc.decoding, dc.type)
        return code


    def __emit_decoding(self, prp, decoding, type):
        """Emits code corresponding to a class property decoding.

        Keyword Arguments:
        prp - property being processed.
        decoding - decoding being applied.
        type - sub type being decoded.

        """
        def get_decoding_function():
            # ... simple/enum types - return type name as this is mapped to a convertor function.
            if prp.type.is_simple or prp.type.is_enum:
                return '\'{0}\''.format(get_type_functional_name(prp.type))
            # ... complex classes - return type functional name.
            elif prp.type.is_class:
                type_name = prp.type.name if type is None else type
                return get_class_decoder_function_name(type_name)

        # Set template.
        tmpl = '{0}(\'{1}\', {2}, {3}, \'{4}\'),'

        # Geenrate code.
        code = tmpl.format(
            emit_line_return() + emit_indent(2),
            prp.name,
            prp.is_iterative,
            get_decoding_function(),
            decoding)

        return code


    def __get_decoder_file_name(self, pkg):
        """Returns name of decoding file.

        Keyword Arguments:
        pkg - package being processed.

        """
        dir = get_ontology_directory(pkg.ontology, self.opts.out_dir, 'decoding', self.opts.out_suffix)
        file = dir +'/'
        file += get_package_decoder_file_name(pkg)
        file += FILE_EXTENSION
        return file


    def __emit_root_package_init_file(self):
        """Emits the root package initialisation file.

        """
        lr = emit_line_return()

        # Open template.
        code = _get_template('decoder_root_package.txt')

        def get_module_exports():
            exports = ''
            is_first = True
            for e in self.ontology.entities:
                if is_first == False:
                    exports += ', '
                cls_decoder = get_class_decoder_function_name(e)
                exports += '\'{0}\''.format(cls_decoder)
                is_first = False
            return exports

        def get_module_imports():
            imports = ''
            is_first = True
            for e in self.ontology.entities:
                if is_first == False:
                    imports += lr
                imports += 'from py{0}.v{1}.decoding.{2} import {3}'.format(
                    get_ontology_name(self.ontology),
                    get_ontology_version(self.ontology),
                    get_package_decoder_file_name(e.package),
                    get_class_decoder_function_name(e))
                is_first = False
            return imports

        # Set helper vars.
        module_exports = get_module_exports()
        module_imports = get_module_imports()

        # Generate code.
        code = inject_standard_template_params(self.ontology, self.opts, code)
        code = code.replace('{module-imports}', module_imports)
        code = code.replace('{module-exports}', module_exports)

        return code
