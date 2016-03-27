=====
sit-builder
=====

sit-builder is a simple Django app to conduct Web-based sit-builder. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. instal the package using "pip install git+git://github.com/ahmadiga/sit-builder.git"

2. Add "sit-builder" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'sit_builder',
    ]