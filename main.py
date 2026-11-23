import os


def main():
    os.makedirs("/output", exist_ok=True)
    line = (
        "v2.4.1: Fixed a bug where 8 hours of sleep still left the user tired. "
        "Battery now charges to 100% instead of 37%."
    )
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
