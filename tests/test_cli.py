# SPDX-License-Identifier: MIT

"""Tests for copa CLI"""

import pytest
from typer.testing import CliRunner

from copa import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.app)
    assert result.exit_code == 0
    
    help_result = runner.invoke(cli.app, ['--help'])
    assert help_result.exit_code == 0
    assert '--help' in help_result.stdout
