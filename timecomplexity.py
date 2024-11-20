import ast
import sys

class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.time_complexity = 'O(1)'
        self.loop_nesting = 0
        self.max_loop_nesting = 0

    def visit_FunctionDef(self, node):
        # Analyze the function body
        self.generic_visit(node)

    def visit_For(self, node):
        # Entering a for loop
        self.loop_nesting += 1
        self.max_loop_nesting = max(self.max_loop_nesting, self.loop_nesting)
        self.generic_visit(node)
        # Exiting the for loop
        self.loop_nesting -= 1

    def visit_While(self, node):
        # Entering a while loop
        self.loop_nesting += 1
        self.max_loop_nesting = max(self.max_loop_nesting, self.loop_nesting)
        self.generic_visit(node)
        # Exiting the while loop
        self.loop_nesting -= 1

    def report(self):
        if self.max_loop_nesting == 0:
            self.time_complexity = 'O(1)'
        else:
            self.time_complexity = f'O(n^{self.max_loop_nesting})'

        print(f"Estimated Time Complexity: {self.time_complexity}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python timecomplexity.py <python_file>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        source = f.read()

    tree = ast.parse(source)
    analyzer = ComplexityAnalyzer()
    analyzer.visit(tree)
    analyzer.report()