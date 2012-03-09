[ES-DOC pycim-mp](http://www.esrl.noaa.gov/cog/es-doc/) - CIM Python Meta-Programming Utility
==================================================

What is ES-DOC ?
--------------------------------------

ES-DOC stands for Earth Science - Documentation.  It's goal is to provide software tools and services in order to support the distribution of earth science documentation.

What is the CIM ?
--------------------------------------

Metafor was a European project tasked with defining a metadata standard for describing scientific processes, particularly climate modelling processes.  This metadata standard came to be known as the CIM (Common Information Model).

What is pycim-mp ?
--------------------------------------

pycim-mp is a CIM meta-progamming utility written in python.  It is an essential part of the CIM eco-system of tools & services that allows developers to work with CIM metadata in the encoding of their choice and in the programming language of their choice.

pycim-mp achieves this by forward engineering code based upon a pythonic representation of the CIM schema.

Why pycim-mp ?
--------------------------------------

CIM metadata is typically encoded in an xml format that is complex in structure and large  in size.  jscim resolves these issues and allows 3rd parties to effortlessly integrate CIM metadata into their websites.

Who uses jscim ?
--------------------------------------

jscim is used by several websites including:
	1. Earth System Grid - Federation peer-to-peer web front end;
	2. IPSL Prodiguer Portal.
	3. KNMI Impacts portal.

What are the contents of jscim ?
--------------------------------------

    \bin                Production js & css files.
    \build              Build script for generating production files.
    \demo\demo.xhtml    Plugin demonstration page.
    \src                Development js & css files.
