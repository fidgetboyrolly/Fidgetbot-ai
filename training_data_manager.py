import re
import os

TRAIN_FILE = "train_data.txt"
MIN_TRAIN_Cimport re
import os

TRAIN_FILE = "train_data.txt"
MIN_TRAIN_COUNT = 100  # Adjust as needed

def standardize_and_fix_entries():
    """Fix existing entries in train_data.txt to standardize keys and tags."""
    if not os.path.exists(TRAIN_FILE):
        return
    with open(TRAIN_FILE, "r", encoding="utf8") as f:
        lines = f.readlines()
    fixed_lines = []
    for line in lines:
        # Standardize tag, keys, and spelling
        fixed = re.sub(r"\[.*?\{", "[train_data{", line)
        fixed = re.sub(r"user_imput:", "user_input:", fixed)
        fixed = re.sub(r"respose:", "response:", fixed)
        fixed = re.sub(r"data;train", "train_data", fixed)
        # Only add if both keys exist
        if "{response:" in fixed and "{user_input:" in fixed:
            # Ensure trailing 'txt]' if missing
            if not fixed.rstrip().endswith("txt]"):
                if fixed.rstrip().endswith("}]"):
                    fixed = fixed.rstrip()[:-2] + "txt]\n"
                else:
                    fixed = fixed.rstrip() + "txt]\n"
            fixed_lines.append(fixed.strip() + "\n")
    with open(TRAIN_FILE, "w", encoding="utf8") as f:
        f.writelines(fixed_lines)

def get_train_count():
    """Count train samples in train_data.txt."""
    if not os.path.exists(TRAIN_FILE):
        return 0
    with open(TRAIN_FILE, "r", encoding="utf8") as f:
        return sum(1 for _ in f if "[train_data{" in _)

def append_to_train_data(user_input, response):
    """Append a standardized training sample."""
    entry = f"[train_data{{response:{response}}}{{user_input:{user_input}}}txt]\n"
    with open(TRAIN_FILE, "a", encoding="utf8") as f:
        f.write(entry)

def bootstrap_with_public_data(public_data_path):
    """Fill up with public data if not enough samples."""
    if get_train_count() < MIN_TRAIN_COUNT and os.path.exists(public_data_path):
        with open(public_data_path, "r", encoding="utf8") as src:
            lines = src.readlines()
        with open(TRAIN_FILE, "a", encoding="utf8") as dest:
            for line in lines:
                dest.write(line)

# Call this once at startup to fix typos in existing file
standardize_and_fix_entries()

# Call this once at startup to fix typos in existing file
standardize_and_fix_entries()
