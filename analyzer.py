
import ast


class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.current_function = None
        self.loop_depth = 0
        self.max_loop_depth = 0
        self.recursive_call_count = 0
        self.recursive = False
        self.memory_allocations = 0
        self.has_early_return = False
        self.has_logarithmic_loop = False

    def visit_FunctionDef(self, node):
        previous_function = self.current_function
        self.current_function = node.name

        # Analyze this function independently.
        self.generic_visit(node)

        self.current_function = previous_function

    def visit_For(self, node):
        self.loop_depth += 1
        self.max_loop_depth = max(
            self.max_loop_depth, self.loop_depth
        )

        # Detect common logarithmic loops such as:
        # while n > 1: n //= 2
        self.generic_visit(node)
        self.loop_depth -= 1

    def visit_While(self, node):
        self.loop_depth += 1
        self.max_loop_depth = max(
            self.max_loop_depth, self.loop_depth
        )

        if self._looks_logarithmic(node):
            self.has_logarithmic_loop = True

        self.generic_visit(node)
        self.loop_depth -= 1

    def _looks_logarithmic(self, node):
        """Recognize some common halving/doubling while loops."""
        for child in ast.walk(node):
            if isinstance(child, ast.AugAssign):
                if isinstance(child.op, (ast.FloorDiv, ast.Div)):
                    if isinstance(child.value, ast.Constant):
                        if child.value.value > 1:
                            return True

                if isinstance(child.op, ast.Mult):
                    if isinstance(child.value, ast.Constant):
                        if child.value.value > 1:
                            return True

        return False

    def visit_Call(self, node):
        if (
            isinstance(node.func, ast.Name)
            and node.func.id == self.current_function
        ):
            self.recursive = True
            self.recursive_call_count += 1

        self.generic_visit(node)

    def visit_Return(self, node):
        if node.value is not None:
            self.has_early_return = True

        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(
            node.value,
            (ast.List, ast.Dict, ast.Set, ast.ListComp,
             ast.DictComp, ast.SetComp, ast.GeneratorExp)
        ):
            self.memory_allocations += 1

        self.generic_visit(node)

    def get_time_complexity_cases(self):
        if self.recursive:
            if self.recursive_call_count >= 2:
                return {
                    "Best": "Input-dependent (recursive)",
                    "Average": "Input-dependent (recursive)",
                    "Worst": "Input-dependent (recursive)"
                }

            return {
                "Best": "Input-dependent (recursive)",
                "Average": "Input-dependent (recursive)",
                "Worst": "Input-dependent (recursive)"
            }

        if self.max_loop_depth == 0:
            return {
                "Best": "O(1)",
                "Average": "O(1)",
                "Worst": "O(1)"
            }

        if self.has_logarithmic_loop:
            complexity = "O(log n)"
        elif self.max_loop_depth == 1:
            complexity = "O(n)"
        else:
            complexity = f"O(n^{self.max_loop_depth})"

        # A loop may return early, but only if the return is
        # reachable before the loop finishes. AST-only analysis
        # cannot reliably establish that for every program.
        best = "O(1)" if self.has_early_return else complexity

        return {
            "Best": best,
            "Average": complexity,
            "Worst": complexity
        }

    def get_space_complexity(self):
        if self.recursive:
            return "Input-dependent (recursion stack)"

        if self.memory_allocations:
            return "Input-dependent (allocated data structures)"

        return "O(1)"
