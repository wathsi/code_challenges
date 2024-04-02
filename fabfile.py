"""
This module contains optimized solution for Advent of Code 2022 - Day 1.
This is a class based solution for learning industrial programming.

Package: code_challenges
Subpackage: aoc/y2k22/day_1
File: calorie_counter.py
Author: Waan <admin@waan.email>
Version: 1.0.0
Created: 01/12/2022
Modified: 01/02/2024 by admin@waan.email
"""

from fabric2 import task
from typing import Any


@task
def autoflake(ctx: Any) -> None:
    """
    Runs the autoflake tool to remove unused imports and variables in the code_challenges directory.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run(
        "autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place code_challenges"
    )


@task
def isort(ctx: Any) -> None:
    """
    Runs the isort tool to sort imports in the code_challenges directory.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run("isort code_challenges")


@task
def black(ctx: Any) -> None:
    """
    Runs the black tool to format the code in the code_challenges directory.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run("black .")


@task
def flake(ctx: Any) -> None:
    """
    Runs the flake8 tool to check for PEP 8 compliance in the code_challenges directory.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run("flake8 .")


@task
def pylint(ctx: Any) -> None:
    """
    Runs the pylint tool to perform static code analysis on the code_challenges directory.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run("pylint code_challenges")


@task
def mypy(ctx: Any) -> None:
    """
    Runs the mypy tool to perform static type checking on the code_challenges directory.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run("mypy code_challenges")


@task
def bandit(ctx: Any) -> None:
    """
    Runs the bandit tool to perform security analysis on the code_challenges directory.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run("bandit -r code_challenges")


@task
def pytest(ctx: Any) -> None:
    """
    Runs pytest to execute the tests in the code_challenges directory and generate a
    coverage report.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run("pytest --cov=code_challenges --cov-report=xml")


@task
def coverage(ctx: Any) -> None:
    """
    Runs coverage to generate a coverage report for the code_challenges directory.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    ctx.run("coverage report --show-missing")


@task
def check(ctx: Any) -> None:
    """
    Runs a series of tasks to check the code quality and test coverage in the code_challenges.

    Parameters:
    -----------
    ctx: Any
        The context object.

    Returns:
    --------
    None
    """
    autoflake(ctx)
    isort(ctx)
    black(ctx)
    flake(ctx)
    pylint(ctx)
    mypy(ctx)
    bandit(ctx)
    pytest(ctx)
    coverage(ctx)
