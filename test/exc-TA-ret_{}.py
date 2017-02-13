'''
Tests subtlety of transitioning between an optional and required arc.
The `as` implies a SETUP_FINALLY block,
which is optional but must jump to the required `return False`.
'''

from exc import *

def top(arg):
  try:
    try_(arg)
  except E1 as e1:
    return True
  return False

handle_args(top)
