Introduction
============

TODO: introduction

Criteria
========

  1. Compliance with PEP-0008 and PEP-0257
  2. Good processes for documentation
  3. Consistency within all ES-DOC projects


Pycim-mp
========

Docstrings
----------

Best code documentation tool is sphinx_.  `Read The Docs`_ is a
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


Module metadata variables
-------------------------

The use of module variables ``__author__``, ``__copyright__``,
``__maintainer__``, etc. is not standard and although valid does not
guarentee interoperability with python code tools.  There is no firm
standard in this area.  Authorship metadata should be present in a
``setup.py`` file.

.. admonition:: Recommendation

   All packages should have a ``setup.py`` file with authorship and
   licensing metadata.  Modules that are intended as scripts should
   define a ``main`` function and declare it as an entry point in
   ``setup.py``.  Making modules callable directly with ``if __name__
   == "__main__"`` is useful for developing but should be avoided for
   the public API.


Code inspection
---------------

1. ``pydoc_mp.core.ontology.package_info.PackageInfo.__init__``

   Use of backslashes to signify line-breaks is error prone and not
   recommended.  Use parentheses instead.

2. Use of new-style formatting strings

   Use of ``str.format()`` makes the code incompatible with Python
   <2.6.  This is fine but should be stated in the packaging metadata


Architecture
------------

.. admonition:: Recommendation

   The meta-programming framework creates it's own templating language.  I recommend using a standard templating library suitable for non-html markup like Jinja2_, Cheetah_ or Genshi_

.. _Jinja2: http://jinja.pocoo.org/docs/
.. _Cheetah: http://www.cheetahtemplate.org
.. _Genshi: http://genshi.edgewall.org


Django-cim-forms
================

.. admonition:: Recommendation

   Installation of this package requires distribute_, a fork of
   setuptools.  This aligns the package with cutting-edge developments
   in Python packaging.  I would recommend *not* requiring distribute
   in ``setup.py`` to remain compatible with setuptools unless
   distribute fixes an issue with installing this package.  If
   requiring distribute is essential you should include
   ``distribute_setup.py`` in the package as documented here_.


.. _distribute: http://pypi.python.org/pypi/distribute
.. _here: http://packages.python.org/distribute/using.html#using-distribute-in-your-project

Docstrings
----------

Module and function-level docstrings are often missing.  Public methods and all modules should have docstrings.

.. admonition:: Recommendation

   The repository path ``django_cim_forms/migrations.bak`` appears to
   be a deprecated or backup module.  If this is the case it need not
   be checked into the the master branch.
