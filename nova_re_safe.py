import re

SAFE_VERSION_RE = re.compile(r"(\d+\.\d+(?:\.\d+)?)$")  # safe, linear-time regex

def check_update(existing_type: str, machine_type: str) -> None:
    # Safe version check — but SonarQube still reports

    # Extract versions (linear-time; no catastrophic backtracking)
    old = SAFE_VERSION_RE.search(existing_type)
    new = SAFE_VERSION_RE.search(machine_type)

    if old and new:
        if tuple(map(int, new.group(1).split("."))) < \
           tuple(map(int, old.group(1).split("."))):
            raise ValueError("Invalid update")


# Main

# check_update("nova 2.1.0", "nova 2.0.5")
check_update("nova 2.1.0", "nova 2.1.0")
print("Safe version check passed.")