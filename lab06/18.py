import difflib


def compare_files(file1_path, file2_path, output_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        file1_content = file1.readlines()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        file2_content = file2.readlines()

    differ = difflib.Differ()
    diff = list(differ.compare(file1_content, file2_content))

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(diff))


file1_path = "first.txt"
file2_path = "second.txt"
output_path = "differences.txt"

compare_files(file1_path, file2_path, output_path)
print(f"Differences between {file1_path} and {file2_path} written to {output_path}.")
