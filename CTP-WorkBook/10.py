from pathlib import Path


def create_configurations():
    Path("mypy.ini").write_text(
        "[mypy]\n"
        "python_version = 3.12\n"
        "check_untyped_defs = True\n"
        "disallow_untyped_defs = True\n"
    )

    Path("Dockerfile").write_text(
        "FROM python:3.12\n"
        "WORKDIR /app\n"
        "COPY . .\n"
        "RUN pip install --no-cache-dir mypy pytest\n"
        "CMD [\"python\", \"main.py\"]\n"
    )

    workflow = Path(".github/workflows")
    workflow.mkdir(parents=True, exist_ok=True)

    (workflow / "ci.yml").write_text(
        "name: Python CI/CD\n\n"
        "on:\n"
        "  push:\n"
        "  pull_request:\n\n"
        "jobs:\n"
        "  test:\n"
        "    runs-on: ubuntu-latest\n\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n\n"
        "      - uses: actions/setup-python@v5\n"
        "        with:\n"
        "          python-version: '3.12'\n\n"
        "      - run: pip install mypy pytest\n"
        "      - run: mypy .\n"
        "      - run: pytest\n"
    )

    print("mypy configuration created")
    print("Docker configuration created")
    print("GitHub Actions CI/CD configuration created")


def main():
    create_configurations()


if __name__ == "__main__":
    main()