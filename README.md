 # Writing the provided user documentation into a Markdown file.

documentation_content = """
# 用户文档 - Markdown文件合并与目录结构管理工具

## 介绍

本程序的设计目的是合并指定源目录下的所有Markdown文件，同时将源目录及其子目录中的文件（不包含文件夹）复制到目标目录中。程序将忽略源目录中的次一级目录，并将次二级目录的内容直接合并到目标目录的次一级目录中。此设计可以确保Markdown文件中引用的任何资源文件（如图片、资产文件夹等）仍然能够正确引用。

## 特点

- **Markdown文件合并**：所有符合条件的Markdown文件内容会被合并至一个指定的Markdown文件中。
- **文件复制**：除了Markdown文件外，源目录中的其他文件会被直接复制到目标目录。
- **目录结构调整**：源目录的次一级目录会被忽略，其次二级目录中的内容直接合并至目标目录的次一级。

## 使用说明

### 环境要求

- Python 3.x
- 具有读写权限的文件系统

### 操作指南

1. **准备**：
   - 确保包含待处理Markdown文件和其他文件的源目录路径是正确的。
   - 确定目标目录路径。程序将内容写入该目录。

2. **运行程序**：
   - 启动Python脚本：
     ```bash
     python merge_tool.py
     ```

3. **提供路径和编码**：
   - 程序将提示输入源目录和目标目录的路径。
   - 提供相关路径后，可输入使用的文件编码格式（默认使用UTF-8）。

4. **程序执行**：
   - 程序将合并Markdown文件，复制其他文件。
   - 完成后，合并的Markdown内容将保存在目标目录下的`merged.md`文件中。

### 示例

假设有以下目录结构： 

**源目录 (`src_directory`)**
```
src/
├── document.md
├── image.png
├── level1/
│ ├── info.md
│ ├── asset/
│ │ ├── image1.jpg
│ │ └── script.js
│ └── sublevel1/
│ ├── details.md
│ └── file.txt
```

**执行效果**

执行程序后，`src/`目录中所有的文件会被拷贝到目标目录 (`dest_directory`)，其中所有的Markdown文件内容会被合并到一个文件中，且目录结构会剥离第一层嵌套夹，结果如下：

**目标目录 (`dest_directory`)**
```
dest/
├── document.md # (原始拷贝)
├── image.png # (原始拷贝)
├── info.md # 在src/level1内找到的
├── asset/
│ ├── image1.jpg # 保留
│ └── script.js # 保留
├── sublevel1/
│ ├── details.md # 同原结构
│ └── file.txt # 同原结构
└── merged.md # 合并后的Markdown
```


`merged.md` 文件将包含 `document.md`、`info.md` 和 `details.md` 的内容。

### 注意事项

- 确保源目录和目标目录都存在，并对用户具有合适的访问权限。
- 如果目标目录中已存在同名文件，程序不会覆盖它们，建议预先清理或检查目录内容。
- 输入的编码必须正确且匹配文件内容，以确保合并和读取过程不出现乱码。
- 上述示例中“次二级”可能对应深度略大以后的文件夹，但程序逻辑上是为了直接处理次二级文件夹中的内容而设计的。

这份文档应该帮助您轻松使用这个程序。如果您有任何问题或建议，欢迎反馈。
"""
