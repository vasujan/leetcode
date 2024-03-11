class solution:
    def customsortstring(self, order: str, s: str) -> str:
        pos = {c: i for i, c in enumerate(order)}

        ordered = [list()] * 27

        for c in s:
            if c in pos:
                if ordered[pos[c]] is None:
                    ordered[pos[c]] = [c]
                else:
                    ordered[pos[c]].append(c)
            else:
                ordered[-1].append(c)
            
        res = []
        for order in ordered:
            if order is not []:
                res.extend(order)
        
        return "".join(res)