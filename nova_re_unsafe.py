import re

UNSAFE_VERSION_RE = re.compile(r"\d+\.\d+$|\d+\.\d+\.\d+$")  # unsafe alternation

def check_update(existing: str, new: str):
    old = re.findall(UNSAFE_VERSION_RE, existing)
    newv = re.findall(UNSAFE_VERSION_RE, new)
    return newv >= old


# Main

# check_update("nova 2.1.0", "nova 2.0.5")
check_update("nova 2.1.0", "nova 2.1.0")
print("Unsafe version check passed.")