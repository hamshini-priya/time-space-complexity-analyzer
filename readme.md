# 📊 Time & Space Complexity Analyzer

A Python-based web application built with **Gradio** that analyzes Python code and estimates its best-case, average-case, and worst-case time complexity, along with space complexity using Abstract Syntax Tree (AST) analysis.

## ✨ Features

- 🔍 Analyze Python code using AST.
- ⚡ Estimate best-case time complexity.
- 🔄 Estimate average-case time complexity.
- 🚨 Estimate worst-case time complexity.
- 🧠 Estimate auxiliary space complexity.
- 🌐 Interactive web interface powered by Gradio.
- ⚠️ Detect invalid Python syntax.

## 🛠️ Technologies Used

- Python
- Gradio
- Abstract Syntax Tree (AST)

## 📁 Project Structure

```text
complexity-analyzer/
├── examples/
├── main.py
├── gradio_app.py
├── parser.py
├── analyzer.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/time-space-complexity-analyzer.git
cd time-space-complexity-analyzer
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If needed, install Gradio directly:

```bash
pip install gradio
```

## ▶️ Run the Application

Start the Gradio interface:

```bash
python gradio_app.py
```

Open the local URL displayed in the terminal, usually:

`http://127.0.0.1:7860`

Paste your Python function into the input box and click **Submit** to view the estimated complexity results.

## 🧪 Example

Input:

```python
def find_item(arr, target):
    for item in arr:
        if item == target:
            return True
    return False
```

Expected theoretical complexity:

| Case | Complexity |
|---|---|
| Best-case time | O(1) |
| Average-case time | O(n) |
| Worst-case time | O(n) |
| Auxiliary space | O(1) |

## ⚠️ Limitations

- Complexity results are estimates based on implemented analysis rules.
- AST-based analysis does not execute the code or fully understand every algorithm.
- Recursive functions, logarithmic loops, and complex control flows may be misclassified.
- Results should be verified for algorithms where accuracy is important.

## 🚀 Future Enhancements

- Improve logarithmic-loop and recursive complexity detection.
- Add support for more control-flow patterns.
- Provide explanations for each complexity result.
- Add more test cases and example algorithms.
- Improve visualization of time and space complexity.

## 🎯 Project Objective

To help students and developers understand algorithm efficiency by providing an interactive tool for estimating the time and space complexity of Python code.

## 👩‍💻 Author

**Hamshini priya S**

## 📄 License

This project is available for educational and learning purposes. Add a formal open-source license if you intend to permit reuse and redistribution.