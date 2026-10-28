from parser import get_ast
from analyzer import ComplexityAnalyzer

def analyze_code(code):
    tree = get_ast(code)
    if tree is None:
        print("❌ Invalid Python code!")
        return

    analyzer = ComplexityAnalyzer()
    analyzer.visit(tree)

    time_complexity = analyzer.get_time_complexity()
    space_complexity = analyzer.get_space_complexity()

    print("\n📊 Estimated Complexities:")
    print(f"⏱️ Time Complexity: {time_complexity}")
    print(f"🧠 Space Complexity: {space_complexity}")

if __name__ == "__main__":
    print("🔍 Paste your Python code below. Press Enter twice to end input:\n")
    code_lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            code_lines.append(line)
        except EOFError:
            break

    code = "\n".join(code_lines)
    analyze_code(code)
