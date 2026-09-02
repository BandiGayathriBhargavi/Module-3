# The Bad Way: Deep Nesting, Poor Naming, and Manual Resource Management
def proc(lst):
    r = []
    f = open("log.txt", "w") # file opened but not closed properly
    for x in lst:
        if x is not None: # We don't handle the case where x is None
            if x > 100:
                tax = x * 0.15
                r.append(tax)
                f.write(f"Processed: {tax}\n")
            else:
                pass
    f.close() # File not closed properly
    return r
print(proc([50, 120, None, 200])) # User-facing output is not clear, and None is not handled
# The Clean Way: Flat Structure, Pythonic built-ins, and Safe Defaults
def taxes(transactions: list) -> list[float]:
    """Extracts 15% tax for transactions over 100 and logs them safely."""
    valid = [t for t in transactions if t and t > 100]  # List comprehension
    with open("log.txt", "w") as log_file:  # Context manager handles closing
        log_file.writelines(f"Processed: {tx * 0.15}\n" for tx in valid)
    return [tx * 0.15 for tx in valid]
print(taxes([50, 120, None, 200]))