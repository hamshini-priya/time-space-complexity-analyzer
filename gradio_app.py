import gradio as gr
from parser import get_ast
from analyzer import ComplexityAnalyzer

def analyze_code(code):
    try:
        tree = get_ast(code)
        if tree is None:
            return "❌ Invalid Python code", "", "", ""
        
        analyzer = ComplexityAnalyzer()
        analyzer.visit(tree)

        time_cases = analyzer.get_time_complexity_cases()
        space_complexity = analyzer.get_space_complexity()

        return time_cases["Best"], time_cases["Average"], time_cases["Worst"], space_complexity

    except Exception as e:
        print("❌ ERROR:", e)
        return "❌ Error", "❌ Error", "❌ Error", "❌ Error"

iface = gr.Interface(
    fn=analyze_code,
    inputs=gr.Textbox(lines=20, label="📄 Paste your Python Code"),
    outputs=[
        gr.Textbox(label="⚡ Best Case Time Complexity"),
        gr.Textbox(label="🔄 Average Case Time Complexity"),
        gr.Textbox(label="🚨 Worst Case Time Complexity"),
        gr.Textbox(label="🧠 Space Complexity")
    ],
    title="📊 Time & Space Complexity Analyzer",
    description="Paste any Python function to estimate its best, average, and worst time complexities along with space complexity.",
    theme="default"
)

if __name__ == "__main__":
    iface.launch()
