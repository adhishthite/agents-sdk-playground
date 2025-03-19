# Agents SDK Playground

## Commands
- Setup: `poetry install`
- Run demo: `poetry run python -m agents_sdk_pg.demo1`
- Run research bot: `poetry run python -m agents_sdk_pg.research_bot.main`
- Run tests: `poetry run pytest`
- Run single test: `poetry run pytest tests/path_to_test.py::test_name`
- Format code: `poetry run black src tests`
- Lint: `poetry run ruff check src tests`

## Style Guidelines
- **Python**: Requires Python >=3.11
- **Imports**: Standard lib first, third-party second, local modules last
- **Typing**: Use type annotations everywhere
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Async**: Extensive use of async/await pattern
- **Error Handling**: Use specific exceptions with proper context
- **Modules**: Organize by functionality in subdirectories
- **Documentation**: Docstrings for all public functions and classes

This codebase uses the OpenAI Agents SDK with asynchronous operations.