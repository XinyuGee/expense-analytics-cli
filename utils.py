def calculate_mean(numbers):
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        return raise ValueError("Empty list")
    return sum(numbers) / len(numbers)


def calculate_std(numbers):
    """Calculate the standard deviation of a list of numbers."""
    if not numbers:
        return raise ValueError("Empty list")
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5
