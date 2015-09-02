"""Configuration for testtube.

Automatically run tests when files change by running: stir

See: https://github.com/thomasw/testtube
"""

from testtube.helpers import Helper, Flake8, Pep257


class Clear(Helper):
    """Clear the screen."""

    command = 'clear'


class Docstrings(Pep257):
    """Lint docstrings."""

    def get_args(self, *args, **kwargs):
        """Return list of arguments to pass to pep257."""
        return super(Docstrings, self).get_args() + ['--ignore=D100,D203']


clear = Clear(all_files=True)
lint = Flake8(all_files=True)
docstrings = Docstrings(all_files=True)

PATTERNS = (
    (r'.*\.py$', [clear, lint, docstrings], {'fail_fast': True}),
)
