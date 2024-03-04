Parallelizing code without Parallelizing
========================================

In this lesson we will introduce the concept of embarassingly parallel code, and how we can use this property
to easily distribute heavy computation to multiple processes without the necessity of falling back on 
mechanisms within the language. 

.. prereq::

   1. General programming knowledge. 

   2. Access to a cluster using the `slurm <https://slurm.schedmd.com/documentation.html>`__ scheduler. 
   
.. csv-table::
   :widths: auto
   :delim: ;

   10 min ; :doc:`motivation`
   10 min ; :doc:`concepts`
   10 min ; :doc:`code_adaptions`
   20 min ; :doc:`array_jobs`
   20 min ; :doc:`submission_by_script`
   5 min ; :doc:`conclusions`


.. toctree::
   :maxdepth: 1
   :caption: The lesson

   motivation
   concepts
   code_adaptions
   array_jobs
   submission_by_script
   conclusions


.. toctree::
   :maxdepth: 1
   :caption: Reference

   exercises
   quick-reference


.. toctree::
   :maxdepth: 1
   :caption: About

   All lessons <https://coderefinery.org/lessons/core/>
   CodeRefinery <https://coderefinery.org/>
   Reusing <https://coderefinery.org/lessons/reusing/>
