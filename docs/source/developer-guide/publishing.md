# Publishing to PyPI

This guide covers how to publish copa releases to the Python Package Index (PyPI).

## Prerequisites

1. **PyPI Account**: Create an account at [pypi.org](https://pypi.org)
2. **API Token**: Generate an API token in your PyPI account settings
3. **Configure Twine**: Run `python -m twine configure` to set up authentication

## Development Dependencies

Install the required build and publishing tools:

```bash
pip install -e .[dev]
```

This installs:
- `build` - Package building tool
- `twine` - PyPI upload tool
- `pytest` - Testing framework

## Release Process

### 1. Update Version

Edit `pyproject.toml` and bump the version number:

```toml
[project]
name = "copa"
version = "0.1.2"  # Update this
```

### 2. Test Locally

Ensure everything works before publishing:

```bash
# Install in editable mode
pip install -e .

# Run tests
pytest

# Test the CLI
copa --help
```

### 3. Build Package

Create distribution files:

```bash
python -m build
```

This creates:
- `dist/copa-X.X.X.tar.gz` (source distribution)
- `dist/copa-X.X.X-py3-none-any.whl` (wheel)

### 4. Upload to PyPI

```bash
python -m twine upload dist/*
```

Enter your PyPI credentials when prompted, or use the configured API token.

## Verification

After publishing, verify the release:

1. Check [pypi.org/project/copa](https://pypi.org/project/copa)
2. Install from PyPI: `pipx install copa==X.X.X`
3. Test basic functionality

## Troubleshooting

### Package Name Already Taken

If "copa" is already taken on PyPI, you may need to:
- Use a different name (e.g., "copa-cli")
- Contact PyPI support to request the name

### Authentication Issues

- Ensure API token has upload permissions
- Verify token is configured correctly with `python -m twine configure`
- Check network connectivity and PyPI status

### Build Errors

- Ensure all files are properly included in `pyproject.toml`
- Check that imports work correctly
- Verify package metadata is complete