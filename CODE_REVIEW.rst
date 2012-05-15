Introduction
============

TODO: introduction


Criteria
========

The general brief was as follows

.. block-quote:

  By code review I mean the totality of the contents of the gut hub
  repo, i.e. source-code, unit/functional tests, & wiki pages
  (i.e. technical documentation).  Basically we are asking how
  professional is the github repo under the spotlight.  In relation to
  python source code the standard python PEP's should be adhered to,
  i.e. http://www.python.org/dev/peps/pep-0008/ and
  http://www.python.org/dev/peps/pep-0257/.  In relation to source code
  we also need input in respect of design, i.e. is the code optimal or
  not, is it well designed into modular packages … etc.

It should be pointed out that PEP8_ is a style guide rather than
coding standard and is primarily designed for guidance in contributing
to the Python standard library.  As such it shouldn't be assumed that
conformance to PEP8_ is the only acceptable way of writing well formed
idiomatic Python.  In particular I draw your attention to the
introductory section of PEP8 `a foolish consistency...'_ which states

.. block-quote:

  A style guide is about consistency. Consistency with this style guide
  is important. Consistency within a project is more
  important. Consistency within one module or function is most
  important.

However, many project take PEP8_ as a starting
point for their coding style.  Similarly PEP257_ offers minimal
guidance for formulating docstrings and any single project is likely
to have more constrained docstring format.

.. _PEP8: http://www.python.org/dev/peps/pep-0008/
.. _PEP257: http://www.python.org/dev/peps/pep-0257/
.. _`a foolish consistency...`: http://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds

Procedure
=========

Given the initial brief and time available I have taken PEP8_ and PEP257_ as the starting
point for classifying what areas to evaluate.  I have conducted an ad
hoc browse of the source to familiarise myself with the general
structure and style from which I have been able to make some general
comments.  Then I used the pylint_ tool to identify potential problems
with the source.  Pylint is a very picky tool which flags many
issues that may be of no real concern, therefore I select which issues
flagged by pylint are worth highlighting.  

During my investigations I annotate the source when ever I find a
programming construct that is a concern using this format:

.. code-block: python

   #!REVIEW: Comment on the code that follows
   #         possibly extended to multiple lines
   

I have made no attempt to annotate all occurences of a construct and I
have not analysed the source in depth.

.. _pylint: http://www.logilab.org/857


Summary Recommendations
=======================

My main recommendations are as follows:

 1. Create a ``setup.py`` file to provide a mechanism for buildint
 tarballs and to define distribution metadata

 2. Start using the sphinx_ documentation system.



Code Review
===========

Distribution and package layout
-------------------------------

The pycim-mp distribution does not contain a ``setup.py`` module script for
packaging the project and providing top-level metadata.  It should be
noted that the existence of module level metadata attributes such as
``__author__`` is not a Python standard, although it is a
relatively common convention, and therefore it is not
a substitute for declaring package metadata in ``setup.py``.  

.. admonition:: Recommendation

   All packages should have a ``setup.py`` file with authorship and
   licensing metadata.  Modules that are intended as scripts should
   define a ``main`` function and declare it as an entry point in
   ``setup.py``.  Making modules callable directly with ``if __name__
   == "__main__"`` is useful for developing but should be avoided for
   the public API.

Modules are consistently laid out with consistent headers to each
source file.  

Documentation and docstrings
----------------------------

There appears to be no documentation other than the ``README.md`` and
docstrings.

The best code documentation tool is sphinx_.  `Read The Docs`_ is a
Github client service that will automatically build your sphinx
documentation and make it public.

Sphinx can be used to create documentation along-side the source,
automatically from docstrings or a mixture of both.  Therefore to make
best use of sphinx docstrings should be formatted using
reStructuredText_.  Beyond this there are no firm requirements on how
parameters are described inside docstrings.  Different projects take
different approaches.  Plain-text is acceptable although `Sphinx
Cross-references`_ are very useful and there are options for formating
parameters.

For instance here is an example of formatted
parameter declarations in declaring the
``pycim_mp.core.class_info.ClassInfo.__init__()`` method:

.. code-block: python

   def __init__(self, name, base, is_abstract, doc_string, properties, decodings):
        """Constructor.

        Keyword Arguments:

	:param name: name (see python conventions).
        :param base: base class used in object hierarchies.
        :param is_abstract: falg indicating whether this is an abstract class or not.
        :param doc_string: documentation string.
        :param properties: set of associated properties.
        :param decodings: set of associated decodings.
        
        """

.. admonition:: Recommendation

   Maintain a ``doc`` directory with Sphinx source in it which builds
   API documentation from the docstrings.  Gradually migrate
   docstrings to be most useful within the Sphinx HTML output.

.. _Sphinx: http://sphinx.pocoo.org
.. _`Read The Docs`: http://read-the-docs.readthedocs.org/en/latest/index.html
.. _reStructuredText: http://sphinx.pocoo.org/rest.html
.. _`Sphinx Cross-references`: http://sphinx.pocoo.org/markup/inline.html#cross-referencing-syntax


Function, class and method docstrings are consistent and conform well
to PEP257.  There are no module-level docstrings which means tools
like ``pydoc`` will not display useful module documentation

.. admonition:: Recommendation

   Add module-level docstrings




Code lay-out
------------

The code is generally very well laid out and easy to read with good
commenting style.  PEP8 recommends keeping all lines to 79 characters
or less and the code often exceeds this threshold.  This restriction
is infamously difficult to stick to and many projects don't attempt
to, however it is considered the gold standard in idiomatic python

.. admonition:: Recommendation

   Decide whether you are going to stick strictly to the PEP8 79
   character limit
  
In some cases the PEP8 recommendation of having a space either side of
``=`` in assignements is not adhered to.  pylint will pick this up.


Imports
-------

The code makes common use of ``from <module> import *``.  This idiom
is generally discouraged in Python because it makes it more difficult
to trace the origin of a definition from within any given source
file.  The consistent use of ``__all__`` within modules partially
mitigates this problem but I would still advise avoiding ``from
<module> import *``.  When there are too many names to import
individually and the package name is long you can define an
abbreviation such as:

.. code-block: python

   # A common example of abbreviating a module import
   import matplotlib.pyplot as plt


Naming Conventions
------------------

The addheres to PEP8 naming conventions very consistently.  The only
exception being fairly widespread use of single character variable
names, which are discouraged.

Module metadata variables
-------------------------

The use of module variables ``__author__``, ``__copyright__``,
``__maintainer__``, etc. is not standard and although valid does not
guarentee interoperability with python code tools.  There is no firm
standard in this area.  Authorship metadata should be present in a
``setup.py`` file.

Python version compatibility
----------------------------

Use of ``str.format()`` makes the code incompatible with Python<2.6.
This is fine but should be stated in the packaging metadata.



Architecture
============

The code makes heavy use of private instance attributes prefixed with
double underscore and property getters and setters.  This level of
data hiding is fairly uncommon in Python source.  The
double-underscore system is primarily intended to protect private
instance attributes from accidental overwriting in subclasses and not to hide
them from instance users.

.. admonition:: Recommendation

   The meta-programming framework creates it's own templating language.  I recommend using a standard templating library suitable for non-html markup like Jinja2_, Cheetah_ or Genshi_

.. _Jinja2: http://jinja.pocoo.org/docs/
.. _Cheetah: http://www.cheetahtemplate.org
.. _Genshi: http://genshi.edgewall.org



