#!/usr/bin/env python
"""Root entrypoint for platforms that expect manage.py at repository root."""
import os
import sys
from pathlib import Path


def main():
    project_dir = Path(__file__).resolve().parent / 'evaluaciones_juan_manuel_miguel_alfaro_carlos_taquez'
    sys.path.insert(0, str(project_dir))
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'evaluaciones_juan_manuel_miguel_alfaro_carlos_taquez.settings',
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
