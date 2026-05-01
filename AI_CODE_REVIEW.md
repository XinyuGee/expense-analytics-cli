# AI Code Review Notes

## File Reviewed
utils.py

## Review Findings

### AI-Catchable Findings
1. The functions return `0` for empty input, which may hide invalid usage instead of making the error explicit.
2. `calculate_std(numbers)` depends on `calculate_mean(numbers)` and should clearly document whether it computes population standard deviation.
3. There is no input validation to ensure the list contains only numeric values.
4. Type hints are missing, which makes the interface less explicit.
5. The empty-input behavior should be tested explicitly because it affects correctness.

### Human-Judgment Findings
1. It is a design decision whether empty input should return `0`, `None`, or raise `ValueError`.
2. It is a product and API decision whether this utility module should be permissive or strict with invalid inputs.
3. The current behavior may be acceptable for a classroom demo, but a production analytics tool would likely want more explicit error handling.

## Conclusion
AI is useful for finding correctness, readability, and validation gaps quickly. However, the decision about what the function *should* do for empty or malformed input still requires human judgment.
