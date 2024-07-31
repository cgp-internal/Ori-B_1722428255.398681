HTML Structure and Syntax Validator
======================================

This repository contains a Python script to validate HTML project structure and syntax using Beautiful Soup and html5lib libraries. The script utilizes the following dependencies:

* `beautifulsoup4`
* `html5lib`

Files and Classes Exposed
-------------------------

* `main.py`: The main Python script to validate HTML project structure and syntax.
* `validators/html_validator.py`: Contains the `HTMLValidator` class that uses Beautiful Soup and html5lib to validate HTML files.
* `models/validation_error.py`: Defines the `ValidationError` class to represent errors and warnings found during HTML validation.
* `loggers/logger.py`: Contains the `Logger` class to log validation errors and warnings to a specified log file.

How to Run
----------

1. Clone the repository and navigate to the project directory.
2. Run `bash run.sh` to install required Python libraries and execute the main script.

Note: Make sure you have Python and bash installed on your system.

The script will validate the HTML project structure and syntax, and log any errors or warnings to a specified log file.