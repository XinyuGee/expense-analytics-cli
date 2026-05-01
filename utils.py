def calculate_mean(numbers):
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_std(numbers):
    """Calculate the standard deviation of a list of numbers."""
    if not numbers:
        return 0
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]
