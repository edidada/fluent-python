"""Run examples stored in directories that are not valid Python package names."""

from pathlib import Path
from runpy import run_path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _run(relative_path):
    run_path(PROJECT_ROOT / relative_path, run_name='__main__')


def spinner_thread_py37():
    _run('18-asyncio-py3.7/spinner_thread.py')


def spinner_asyncio_py37():
    _run('18-asyncio-py3.7/spinner_asyncio.py')


def countdown_py37():
    _run('18-asyncio-py3.7/countdown.py')


def tcp_charfinder_py37():
    _run('18-asyncio-py3.7/charfinder/tcp_charfinder.py')


def charfinder_py37():
    _run('18-asyncio-py3.7/charfinder/charfinder.py')
