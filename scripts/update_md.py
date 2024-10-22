# Write a function to update the README.md file with the list of all the solutions in the solutions folder. Every solutions folder has the README.md file which needs to be linked in the main readme file

import os
from pathlib import Path
from typing import List

def get_solutions():
    """Get the list of solutions in the solutions folder."""
    solutions = []
    for solution in Path('solutions').iterdir():
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
        f.writelines(lines[:start_line + 1])
        f.writelines(solutions_str)
        f.writelines(lines[end_line:])

"""# Leetcode solutions

Solutions to the Leetcode problems.

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problemset/)
"""


# Update the README.md file with the list of all the solutions in the solutions folder
if __name__ == "__main__":
    # print(get_solutions())
    update_readme()