import datetime

def create(file_path, text, metadata=None):
    with open(file_path, "w") as f:
        f.write("Ragul-FILE\n")

        if metadata:
            for key, value in metadata.items():
                f.write(f"{key}: {value}\n")  # Added newline for better formatting

        else:
            f.write(f"Created: {datetime.datetime.now()}\n")

        f.write("~~~~END-META~~~~\n")
        f.write(f"CONTENT:\n{text}\n")
        f.write("~~~~END-CONTENT~~~~~\n")

def read(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    if lines[0].strip() != "Ragul-FILE":
        raise ValueError("Not a valid .ragul file!")

    reading_meta = True
    reading_content = False
    metadata = {}
    content = ""

    for line in lines[1:]:
        if line.strip() == "~~~~END-META~~~~":
            reading_meta = False
            reading_content = True
            continue

        if line.strip() == "~~~~END-CONTENT~~~~~":
            break

        if reading_meta:
            key_value = line.strip().split(": ", 1)  # Split line
            if len(key_value) == 2:  # Check if there are exactly 2 parts
                key, value = key_value
                metadata[key] = value
            else:
                print(f"Skipping invalid metadata line: {line.strip()}")  # Log the invalid line
        elif reading_content:
            content += line

    print("Metadata:", metadata)
    print("Content:", content.strip())

if __name__ == "__main__":
    while True:
        action = input("create or read [Enter 0 to exit] (c/r/0): ").strip().lower()
        if action == "0":
            print("Exited!")
            break

        elif action == "c":
            file_name = input("Enter file name (with .ragul extension): ").strip()
            text = input("Enter text content: ").strip()

            metadata = {}
            metadata["Created"] = str(datetime.datetime.now())
            create(file_name, text, metadata)
            print("File Creation Successful!")

        elif action == "r":
            file_name = input("Enter the file name (with .ragul extension): ").strip()
            try:
                read(file_name)  # No need to unpack as it directly prints metadata and content
            except Exception as e:
                print(f"Error reading file: {e}")

        else:
            print("Invalid. Please choose 'c' or 'r': ")
