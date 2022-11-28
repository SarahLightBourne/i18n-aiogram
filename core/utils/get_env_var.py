from os import environ
from .exceptions import MissingEnvVariable


def get_env_var(variable_name: str, default: str = None, raise_exception: bool = True) -> str:

  if not (variable := environ.get(variable_name, default)):
    if raise_exception:
      raise MissingEnvVariable(f'<{variable_name}> is missing')

  return variable
