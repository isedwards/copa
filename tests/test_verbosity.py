# SPDX-License-Identifier: MIT

"""Tests for copa.core.logging.verbosity module"""

import logging
import pytest

from copa.core.logging.verbosity import get_logging_level


class TestVerbosity:
    """Tests for logging verbosity functionality"""

    def test_count_based_verbosity(self):
        """Test count-based verbosity flags (-v, -vv, -vvv)"""
        assert get_logging_level(['-v']) == logging.WARNING
        assert get_logging_level(['-vv']) == logging.INFO
        assert get_logging_level(['-vvv']) == logging.DEBUG
        
    def test_level_based_verbosity(self):
        """Test level-based verbosity options (--verbosity=level)"""
        assert get_logging_level(['--verbosity=info']) == logging.INFO
        assert get_logging_level(['--verbosity=debug']) == logging.DEBUG
        assert get_logging_level(['--verbosity=warning']) == logging.WARNING
        assert get_logging_level(['--verbosity=error']) == logging.ERROR
        
    def test_numeric_verbosity(self):
        """Test numeric verbosity options (--verbosity=2)"""
        assert get_logging_level(['--verbosity=2']) == logging.INFO
        assert get_logging_level(['--verbosity=5']) == logging.DEBUG  # Clamped to max
        
    def test_level_overrides_count(self):
        """Test that level-based verbosity overrides count-based"""
        assert get_logging_level(['-v', '--verbosity=debug']) == logging.DEBUG
        
    def test_invalid_verbosity(self):
        """Test invalid verbosity defaults to ERROR"""
        assert get_logging_level(['--verbosity=invalid']) == logging.ERROR
        
    def test_default_verbosity(self):
        """Test default verbosity is ERROR when no options provided"""
        assert get_logging_level([]) == logging.ERROR