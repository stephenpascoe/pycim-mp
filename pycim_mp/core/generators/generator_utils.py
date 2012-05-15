"""Base class encapsulating functionality common to all cim code generators.

"""
# Module imports.
import datetime
import os
import sys


# Module exports.
__all__ = ['convert_to_camel_case', 'convert_to_pascal_case',
           'get_template', 'create_directory', 'inject_standard_template_params',
           'emit_indent', 'emit_line_return', 'write_file']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


# Set of loaded templates.
_loaded_templates = dict()


def convert_to_camel_case(name, separator='_'):
    """Converts passed name to camel case.

    Keyword Arguments:
    name - a name as specified in onology spec.
    separator - separator to use in order to split name into constituent parts.

    """
    r = ''
    if name is not None:
        s = name.split(separator)
        for s in s:
            if (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]
    return r


def convert_to_pascal_case(name, separator='_'):
    """Converts passed name to camel case.

    Keyword Arguments:
    name - a name as specified in onology spec.
    separator - separator to use in order to split name into constituent parts.

    """
    r = ''
    s = convert_to_camel_case(name, separator)
    if (len(s) > 0):
        r += s[0].lower()
        if (len(s) > 1):
            r += s[1:]
    return r


def _get_template_path(filename, lang, generator):
    """Returns code template file path.

    Keyword Arguments:
    filename - code template filename.
    lang - genrator being executed.
    lang - target programming language.

    """
    path = None
    # TODO replace with config
    for p in sys.path:
        if p.endswith('pycim-mp/pycim_mp'):
            path = p
            path += '/core/templates/{0}/{1}/'.format(lang, generator)
            path += filename
    return path


def get_template(filename, lang, generator):
    """Returns code template.

    Keyword Arguments:
    filename - code template filename.
    lang - genrator being executed.
    lang - target programming language.

    """
    path = _get_template_path(filename, lang, generator)
    if path not in _loaded_templates:
        tmpl = open(path)
        code = tmpl.read()
        tmpl.close()
        _loaded_templates[path] = code
    return _loaded_templates[path]


def get_username():
    """Returns name of current user.

    """
    username = None
    try:
        import pwd
        username = pwd.getpwuid(os.getuid()).pw_name
    except ImportError:
        username = os.environ.get("USERNAME")
    return username


def emit_indent(count=1):
    """Emits code corresponding to a code indentation.

    Keyword Arguments:
    count - number of indentations to emit.

    """
    code = ''
    for i in range(count):
        code += '    '
    return code


def emit_line_return(count=1):
    """Emits code corresponding to a code line return.

    Keyword Arguments:
    count - number of line returns to emit.

    """
    code = ''
    for i in range(0, count):
        code += '\n'
    return code


def create_directory(dir):
    """Generates a directory into which code will be generated.

    Keyword Arguments:
    dir - target code generation directory.

    """
    try:
        os.makedirs(dir)
    except:
        #!REVIEW: Consider "except IOError"
        pass


def write_file(content, file):
    """Writes code to a file.

    Keyword Arguments:
    content - file content to be written.
    file - path of file to be written.

    """
    file = open(file, 'w')
    file.writelines(content)
    file.close()


def inject_standard_template_params(ont, opts, code):
    """Injects set of standard templates parameters into passed code.

    Keyword Arguments:
    ont - ontology being parsed.
    opts - code generation options.
    code - code derived from template.

    """
    # Library related params.
    code = code.replace('{out-author}', opts.out_author)
    code = code.replace('{out-copyright}', 'Copyright {0} - {1}.'.format(str(datetime.datetime.now().year), opts.out_owner))
    code = code.replace('{out-license}', opts.out_license)
    code = code.replace('{out-maintainer}', opts.out_maintainer)
    code = code.replace('{out-maintainer-email}', opts.out_maintainer_email)
    code = code.replace('{out-owner}', opts.out_owner)
    code = code.replace('{out-version}', opts.out_version)
    code = code.replace('{out-status}', opts.out_status)

    # Onotlogy related params,
    code = code.replace('{ontology-name}', ont.name)
    code = code.replace('{ontology-version}', ont.version)

    # Misceallaneous params.
    code = code.replace('{datetime-now}', str(datetime.datetime.now()))
    code = code.replace('{datetime-year}', str(datetime.datetime.now().year))
    code = code.replace('{user-name}', get_username())

    return code
