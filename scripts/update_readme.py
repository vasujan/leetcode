"""
Write a function to update the README.md file with the list of all the solutions
in the solutions folder. Every solutions folder has the README.md file which
needs to be linked in the main readme file
"""

from pathlib import Path


def get_solutions():
    """Get the list of solutions in the solutions folder."""
    solutions = []
    for solution in Path("solutions").iterdir():
        if solution.is_dir():
            solutions.append(solution.name)
    return sorted(solutions)


def update_readme():
    """Update the README.md file with the list of all the solutions in the solutions folder."""
    # Get the list of solutions
    solutions = get_solutions()
    solutions = [f"- [{solution}](solutions/{solution}/)" for solution in solutions]

    # Create a string with the list of solutions
    solutions_str = "\n".join(solutions) + "\n"

    with open("README.md", "r") as f:
        lines = f.readlines()

    # Find the line numbers of the start and end tags
    start_line = None
    end_line = None

    # find "<!-- solutions_start -->" in the readme file
    for i, line in enumerate(lines):
        if line.strip() == "<!-- solutions_start -->":
            start_line = i
        if line.strip() == "<!-- solutions_end -->":
            end_line = i
            break

    # Write the string to the README.md file
    with open("README.md", "w") as f:
        assert start_line is not None, "Start tag not found in README.md"
        assert end_line is not None, "End tag not found in README.md"
        f.writelines(lines[: start_line + 1])
        f.writelines(solutions_str)
        f.writelines(lines[end_line:])


# Update the README.md file with the list of all the solutions in the solutions folder
if __name__ == "__main__":
    # print(get_solutions())
    update_readme()
