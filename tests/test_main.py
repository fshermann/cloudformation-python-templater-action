import os

from src.main import example


def test_main():
    example(template_path="tests/templates/raw/example.yaml")
