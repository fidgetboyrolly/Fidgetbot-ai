import re
import os
import requests

TRAIN_FILE = "train_data.txt"
DATASET_LINK_FILE = "public_dataset_link.txt"
ALT_PUBLIC_DATA = "alternate_public_train_data.txt"
MIN_TRAIN_COUNT = 100  # Adjust as needed

def standardize_and_fix_entries():
    if not os.path.exists(TRAIN_FILE):
        return
    with open(TRAIN_FILE, "r", encoding="utf8") as f:
        lines = f.readlines()
    fixed_lines = []
    for line in lines:
        fixed = re.sub(r"\[.*?\{", "[train_data{", line)
        fixed = re.sub(r"user_imput:", "user_input:", fixed)
        fixed = re.sub(r"respose:", "response:", fixed)
        fixed = re.sub(r"data;train", "train_data", fixed)
        if "{response:" in fixed and "{user_input:" in fixed:
            if not fixed.rstrip().endswith("txt]"):
                if fixed.rstrip().endswith("}]"):
                    fixed = fixed.rstrip()[:-2] + "txt]\n"
                else:
                    fixed = fixed.rstrip() + "txt]\n"
            fixed_lines.append(fixed.strip() + "\n")
    with open(TRAIN_FILE, "w", encoding="utf8") as f:
        f.writelines(fixed_lines)

def get_train_count():
    if not os.path.exists(TRAIN_FILE):
        return 0
    with open(TRAIN_FILE, "r", encoding="utf8") as f:
        return sum(1 for _ in f if "[train_data{" in _)

def append_to_train_data(user_input, response):
    entry = f"[train_data{{response:{response}}}{{user_input:{user_input}}}txt]\n"
    with open(TRAIN_FILE, "a", encoding="utf8") as f:
        f.write(entry)

def download_public_dataset():
    if not os.path.exists(DATASET_LINK_FILE):
        return
    with open(DATASET_LINK_FILE, "r", encoding="utf8") as f:
        url = f.read().strip()
    if not url:
        return
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(ALT_PUBLIC_DATA, "w", encoding="utf8") as out:
            out.write(response.text)
    except Exception as e:
        print(f"Failed to download public dataset: {e}")

def bootstrap_with_public_data():
    if get_train_count() < MIN_TRAIN_COUNT:
        if not os.path.exists(ALT_PUBLIC_DATA):
            download_public_dataset()
        if os.path.exists(ALT_PUBLIC_DATA):
            with open(ALT_PUBLIC_DATA, "r", encoding="utf8") as src:
                lines = src.readlines()
            with open(TRAIN_FILE, "a", encoding="utf8") as dest:
                for line in lines:
                    dest.write(line)

standardize_and_fix_entries()
