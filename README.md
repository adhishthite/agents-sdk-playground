# Agents SDK Playground

A Python-based playground for experimenting with and developing AI agents using the OpenAI Agents SDK. This project serves as a testing ground for building and evaluating different agent architectures and behaviors.

## Overview

This project provides a structured environment for working with AI agents, specifically focusing on the OpenAI Agents framework. It includes various demo implementations and research components to explore different agent capabilities and interactions.

## Requirements

- Python 3.11 or higher
- Poetry for dependency management

## Key Dependencies

- `openai-agents`: Core framework for agent development
- `python-dotenv`: Environment variable management
- `rich`: Enhanced terminal output formatting

## Project Structure

```
.
├── src/
│   └── agents_sdk_pg/
│       ├── research_bot/    # Research-focused agent implementations
│       ├── demo1.py         # Basic agent demonstration
│       ├── demo1-az.py      # Azure-specific agent demonstration
│       ├── demo2.py         # Advanced agent features
│       └── demo3.py         # Extended agent capabilities
├── tests/                   # Test suite directory
├── poetry.lock             # Locked dependencies
└── pyproject.toml          # Project configuration
```

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Set up your environment variables in `.env`
4. Run the demo scripts:
   ```bash
   poetry run python -m agents_sdk_pg.demo1
   ```

## Development

This project uses Poetry for dependency management. To add new dependencies:

```bash
poetry add package-name
```

## License

[License information not specified]

## Author

Adhish Thite (adhish.thite@gmail.com)
