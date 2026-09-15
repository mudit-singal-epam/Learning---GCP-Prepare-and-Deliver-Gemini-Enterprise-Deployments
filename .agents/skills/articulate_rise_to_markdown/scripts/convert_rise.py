#!/usr/bin/env python3
"""
Entry point for the Articulate Rise to Markdown conversion script.
This script simply delegates to the modular 'rise_converter' package to maintain the Single Responsibility Principle.
"""
from rise_converter.main import main

if __name__ == "__main__":
    main()
