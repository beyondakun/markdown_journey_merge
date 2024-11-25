import os
import shutil

def merge_markdown_and_copy(src_dir, dest_dir, encoding='utf-8', merged_filename='merged.md'):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    markdown_files = []

    # Step 1: 复制源目录中的所有文件（不含文件夹）到目标目录
    for item in os.listdir(src_dir):
        full_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(full_path):
            if full_path.endswith('.md'):
                markdown_files.append(full_path)
            # 复制源目录的文件到目标目录
            if not os.path.exists(dest_path):
                shutil.copy2(full_path, dest_path)

    # Step 2: 遍历源目录的次一级目录，并处理次二级目录
    for first_level_dir in os.listdir(src_dir):
        full_first_level_dir = os.path.join(src_dir, first_level_dir)

        if os.path.isdir(full_first_level_dir):
            for dirpath, dirnames, filenames in os.walk(full_first_level_dir):
                # 获取相对于次一级目录的路径
                rel_path = os.path.relpath(dirpath, full_first_level_dir)

                # 在目标目录中，把次二级的内容作为次一级目录
                dest_subdir = os.path.join(dest_dir, rel_path)

                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)

                for filename in filenames:
                    src_file = os.path.join(dirpath, filename)
                    dest_file = os.path.join(dest_subdir, filename)

                    if filename.endswith('.md'):
                        markdown_files.append(src_file)

                    if not os.path.exists(dest_file):
                        shutil.copy2(src_file, dest_file)

    # 合并所有Markdown文件的内容到一个文件
    merged_file_path = os.path.join(dest_dir, merged_filename)
    with open(merged_file_path, 'w', encoding=encoding) as outfile:
        for md_file in markdown_files:
            with open(md_file, 'r', encoding=encoding) as infile:
                outfile.write(infile.read() + "\n\n")

if __name__ == "__main__":
    print("请输入源文件夹路径：")
    src_directory = input().strip()
    print("请输入目标文件夹路径：")
    dest_directory = input().strip()
    print("请输入文件编码（默认UTF-8，如需其他编码格式请指定）：")
    file_encoding = input().strip() or 'utf-8'
    
    if not os.path.exists(src_directory):
        print(f"源目录路径无效: {src_directory}")
    else:
        try:
            merge_markdown_and_copy(src_directory, dest_directory, encoding=file_encoding)
            print(f"所有Markdown文件已合并，结果保存在 {dest_directory}/merged.md")
        except Exception as e:
            print(f"合并过程中出现错误: {e}")
