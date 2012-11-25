To use this script you require the sourcecode from src/ and the Antlr runtime that matches the lexer and parser code. Currently this is version antlr-3.4.tar.gz available from http://www.antlr.org/download/ or from the libs directory of this project.

INSTALL
=======
The best way to use the software is within a virtualenv. Install python on your machine then install pip and virtualenv, e.g.

Install pip 

    $ sudo easy_install pip

Install virtualenv

    $ pip install virtualenv

Now get the dgdl sourcecode.

    $ git clone https://github.com/siwells/DGDL.git

Change into the dgdl python directory:

    $ cd DGDL/tools/dgdl/

Create a virtualenv to hold the dgdl python program:

    $ virtualenv env

Navigate into the virtualenv and activate it:

    $ cd env
    $ source bin/activate

Now install the runtime to your virtualenv using the version of python install within the virtualenv and the setup.py file from within the lib:

    $ cd ../libs
    $ unzip antlr_python.zip
    $ ../bin/python setup.py install

You can now run the dgdl.py application as follows:

    $ python src/dgdl.py input.dgdl

where input.dgdl is a dgdl game description that you want to process. For further information about using the dgdl.py script see the USAGE section.

When you are finished with the dgdl program deactivate your virtualenv:

    $ deactivate


USAGE
=====

    $ python src/dgdl.py input.dgdl

If the game description is syntactically correct then you will see a pretty printed version of the grammar's AST. If the description is invalid then you will get an error message indicating the source of the problem, e.g.

    > src/broken.dgdl line 1:0 no viable alternative at input u'ssystem'
