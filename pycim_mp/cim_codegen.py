"""Encapsulates CIM meta-programming code generation functions.

"""
# Module imports.
import optparse

from pycim_mp.core.ontology import *
from pycim_mp.core.ontology.utils import create_ontology
from pycim_mp.core.ontology.utils import validate_ontology_config
from pycim_mp.core.generators.utils import create_directory
from pycim_mp.core.cim_exception import CIMException


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



def _get_options():
    """Returns command line option parser.

    """
    # Instantiate option parser.
    p = optparse.OptionParser(prog="CIM Code Generator", version="%prog 1.0 alpha-1")
    p.description = "The CIM code generation utility is a meta-programming tool that generates machine executable code in an array of programming languages such as python, java ...etc.\n"
    p.description += "It is designed to standardize and simplify programming libraries built ontop of CIM standards."

    input = optparse.OptionGroup(p, "Input Options")
    input.add_option("-c", "--cim",
                 action="store", dest="cim",
                 type="choice", choices=["1.5"], default="1.5",
                 help="Target cim version. [default = %default] [choices = 1.5]")
    input.add_option("-l", "--lang","--language",
                 action="store", dest="lang",
                 type="choice", choices=["python"], default="python",
                 help="Target programming languages. [default = %default] [choices = python]")
    input.add_option("-g", "--gen", "--generator",
                 action="store", dest="generator",
                 type="choice", choices=["all", "types", "decoders"], default="all",
                 help="Target code generator to be run. [default = %default] [choices = all | types | decoders]")
    p.add_option_group(input)
    
    output = optparse.OptionGroup(p, "Output Options")
    output.add_option("-o", "--od","--out-dir",
                 action="store", dest="out_dir",
                 type="string", default="/Users/markmorgan/Development/tmp/pycim",
                 help="Target directory into which code will be generated. [default = %default]")
    output.add_option("--osfx", "--out-suf", "--out-suffix",
                 action="store", dest="out_suffix",
                 type="choice", choices=["true", "false"], default="false",
                 help="Flag indicating whether to add to the output directory a suffix. [default = %default] [choices = true | false]")
    output.add_option("--oa", "--out-author",
                 action="store", dest="out_author",
                 type="string", default="Mark Morgan",
                 help="Library author (i.e. developer responsible for code). [default = %default]")
    output.add_option("--ol", "--out-license",
                 action="store", dest="out_license",
                 type="string", default="GPL",
                 help="License under which library will be published. [default = %default]")
    output.add_option("--om", "--out-maintainer",
                 action="store", dest="out_maintainer",
                 type="string", default="Mark Morgan",
                 help="Library maintainer (i.e. developer responsible for code). [default = %default]")
    output.add_option("--ome", "--out-maintainer-email",
                 action="store", dest="out_maintainer_email",
                 type="string", default="momipsl@ipsl.jussieu.fr",
                 help="Email address of library maintainer. [default = %default]")
    output.add_option("--oo", "--out-owner",
                 action="store", dest="out_owner",
                 type="string", default="Institut Pierre Simon Laplace",
                 help="Library owner (i.e. group or institute funding library development). [default = %default]")
    output.add_option("--ov", "--out-version",
                 action="store", dest="out_version",
                 type="string", default="1.5.0",
                 help="Library version (major, minor, revision : e.g. 1.5.0). [default = %default]")
    output.add_option("--ost", "--out-status",
                 action="store", dest="out_status",
                 type="choice", choices=["Alpha", "Beta", 'Production'], default="Production",
                 help="Library status. [default = %default] [choices = Alpha | Beta | Production]")
    p.add_option_group(output)

    # Parse & validate options (n.b. optparse intercepts most validation errors)..
    opts, args = p.parse_args()
    _validate_out_dir(opts.out_dir)

    print "CIM CODE-GEN :: OPTIONS : cim - {0}; languages - {1}; generators - {2}; output-directory - {3}; output-suffux - {4}; output-author - {5}; output-license - {6}; output-maintainer - {7}; output-maintainer email - {8}; output-owner - {9}; output-version - {10}; output-status - {11}.".format(
        opts.cim, opts.lang, opts.generator, opts.out_dir, opts.out_suffix, opts.out_author, opts.out_license, opts.out_maintainer, opts.out_maintainer_email, opts.out_owner, opts.out_version, opts.out_status)
    return opts



def _validate_out_dir(out_dir):
    """Validates user specified output directory.

    Keyword Arguments:
    out_dir - target directory into which generated code will be written.

    """
    import os
    
    # Error if not creatable.
    try:
        create_directory(out_dir)
    except:
        raise CIMException('Output directory ({0}) is an invalid path.'.format(out_dir))
    
    # Error if not created.
    if os.path.exists(out_dir) == False:
        raise CIMException('Output directory ({0}) is an invalid path.'.format(out_dir))



def _get_ontology_config(opts):
    """Returns target ontology from which code will be generated.

    Keyword Arguments:
    opts - code generation options.

    """
    if opts.cim == '1.5':
        from pycim_mp.v1_5 import ontology as cim_v1_5_ontology
        return cim_v1_5_ontology


def _get_generators(opts):
    """Returns filtered collection of generators.

    Keyword Arguments:
    opts - code generation options.

    """
    from pycim_mp.core.generators.python.types.types_generator import TypesGenerator as PythonTypesGenerator
    from pycim_mp.core.generators.python.decoders.decoders_generator import DecodersGenerator as PythonDecodersGenerator

    result = dict()

    # Populate as per target options.    
    if opts.lang == 'python':
        result['types'] = PythonTypesGenerator
        result['decoders'] = PythonDecodersGenerator

    # Exclude others if not requesting all.
    if opts.generator != "all":
        result = dict({ opts.generator : result[opts.generator] })

    return result



def _main():
    """Main entry point.

    """
    # Get options.
    opts = _get_options()

    # Validate ontology config.
    cfg = _get_ontology_config(opts)
    cfg_errors = validate_ontology_config(cfg)
    if len(cfg_errors) > 0:
        for error in cfg_errors:
            print 'CIM CODE-GEN :: ONTOLOGY VALIDATION WARNING :: {0}'.format(error)
        raise CIMException('Ontology configuration contains errors & therefore cannot be parsed.')

    # Instantiate ontology.
    o = create_ontology(cfg)

    # Inform user.
    print 'CIM CODE-GEN :: BEGINS'
    msg = "CIM CODE-GEN :: PROCESSING ONTOLOGY :: {0} ({1} packages, {2} classes, {3} enums)"
    print msg.format(str(o).upper(), len(o.packages), len(o.classes), len(o.enums))

    # Execute generators.
    generators = _get_generators(opts)
    for key in generators:
        generator = generators[key](o, opts)
        generator.execute()
        msg = "CIM CODE-GEN :: EXECUTED GENERATOR :: {0} (lang - {1})"
        print msg.format(key.upper(), opts.lang.lower())
        
    # Inform user.
    print 'CIM CODE-GEN :: COMPLETE'


# Command line entry point.
if __name__ == "__main__":
    _main()
    try:
        _main()
    except CIMException as e:
        print e
    except Exception as e:
        print "CIM CODE-GEN :: ERROR :: !!! UNEXPECTED EXCEPTION !!! :: {0}.".format(e)

