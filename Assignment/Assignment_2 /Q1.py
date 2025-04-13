def find_peak(N: int) -> int:
    """
    Finds the peak index in a unimodal sequence using binary search.

    Args:
        N: Maximum index value (0 to N)

    Returns:
        Index of the peak value
    """
    left, right = 0, N

    while left < right:
        mid = (left + right) // 2
        if query(mid) < query(mid + 1):
            left = mid + 1
        else:
            right = mid

    return left


# Example query function (can be replaced with any unimodal function)
def query(x: int) -> int:
    """Example unimodal function with peak at x=7"""
    return -(x - 7) ** 2 + 49


# Test case
peak = find_peak(15)
print(f"The peak is at position {peak} with value {query(peak)}")
