from validators.html_validator import HTMLValidator
from models.validation_error import ValidationError
from loggers.logger import Logger

def main(logger: Logger, validator: HTMLValidator) -> None:
    try:
        files = ['index.html']  # replace with your list of HTML files
        for file in files:
            validator.validate(file)
            errors = validator.get_errors()
            for error in errors:
                if error['type'] == 'HTMLParserError':
                    logger.error(ValidationError(f'Failed to parse {file}: {error["error"]}'))
                else:
                    logger.error(ValidationError(f'General exception occurred while parsing {file}: {error["error"]}'))
    except Exception as e:
        logger.error(ValidationError(f'An unexpected error occurred: {str(e)}'))

def create_logger() -> Logger:
    return Logger('validation_log.txt')

def create_validator() -> HTMLValidator:
    return HTMLValidator()

if __name__ == '__main__':
    logger = create_logger()
    validator = create_validator()
    main(logger, validator)