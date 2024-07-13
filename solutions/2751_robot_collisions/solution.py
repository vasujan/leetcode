class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = map(list, zip(range(n), positions, healths, directions))
        s_robots = sorted(robots, key=lambda x: x[1])
        print(s_robots)
        stack = []
        for r in s_robots:
            if r[3] == 'L' :
                while stack and stack[-1][3] == 'R':
                    if stack[-1][2] < r[2]:
                        stack.pop()
                        r[2] -= 1
                    elif stack[-1][2] == r[2]:
                        stack.pop()
                        break
                    else:
                        stack[-1][2] -= 1
                        break
                else:
                    stack.append(r)
            else:
                stack.append(r)

        print(stack)

        return [x[2] for x in sorted(stack, key=lambda x: x[0])]
