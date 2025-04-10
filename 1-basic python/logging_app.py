import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler("1-basic python/app.log"), logging.StreamHandler()],
)

logger = logging.getLogger("ArithmaticApp")


def add(a, b):

    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result


def sub(a, b):

    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result


def multipy(a, b):

    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result


def division(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except:
        logger.error("Exception occurred during division")
        return None


add(5, 2)
sub(5, 2)
multipy(5, 2)
division(10, 0)
division(10, 2)