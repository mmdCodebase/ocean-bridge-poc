import functools
import logging
import asyncio

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ocean-bridge-backend")

def log_function_call(func):
    """
    A decorator that logs function calls.
    """
    @functools.wraps(func)  # Preserves the wrapped function's metadata
    def wrapper(*args, **kwargs):
        logger.info(f"Starting '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        try:
            value = func(*args, **kwargs)
            logger.info(f"Function '{func.__name__}' completed successfully")
            return value
        except Exception as e:
            logger.exception(f"Error in function '{func.__name__}': {e}")
            raise  # Re-throw the exception after logging it
    
    return wrapper

def log_function_call_async(func):
    """
    A decorator for logging async function calls.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        logger.info(f"Starting async '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        try:
            value = await func(*args, **kwargs)
            logger.info(f"Async function '{func.__name__}' completed successfully")
            return value
        except Exception as e:
            logger.exception(f"Error in async function '{func.__name__}': {e}")
            raise  # Re-throw the exception after logging it
    
    return wrapper
