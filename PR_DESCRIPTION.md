## Summary
This change adds a utility module for basic statistical calculations used by the Expense Analytics CLI project. The purpose is to separate reusable numeric helper logic from the main command-line entry point so the project has a cleaner structure and is easier to extend later.

## Changes
- created the `feature/add-utils` branch
- added `calculate_mean(numbers)`
- added `calculate_std(numbers)`
- kept the logic small and reusable for later integration into the CLI workflow

## How to Test
Run Python interactively or import the functions from `utils.py`. Verify that `calculate_mean([1, 2, 3])` returns `2.0`. Verify that `calculate_std([1, 2, 3])` returns a numeric result. Also verify that empty input currently returns `0` instead of crashing.
