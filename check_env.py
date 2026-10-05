import platform
import sys
def main() -> None:
    in_venv = sys.prefix != sys.base_prefix
    print(f"Python version : {platform.python_version()}")
    print(f"Interpreter : {sys.executable}")
    print(f"Virtual env : {'yes' if in_venv else 'NO - use uv run'}")
if __name__ == "__main__":
    main()
