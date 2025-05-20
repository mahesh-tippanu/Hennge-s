def main():
    import sys

    def process_case(x_str, y_str):
        try:
            x = int(x_str.strip())
        except:
            return "-1"
        y_split = y_str.strip().split()
        if len(y_split) != x:
            return "-1"
        def recur(idx, acc):
            if idx == x:
                return acc
            try:
                val = int(y_split[idx])
            except:
                return "-1"
            if val > 0:
                return recur(idx+1, acc)
            return recur(idx+1, acc + val**4)
        result = recur(0, 0)
        if result == "-1":
            return "-1"
        return str(result)

    lines = sys.stdin.read().splitlines()
    def process_input(idx, acc, n):
        if n == 0:
            return acc
        if idx+1 >= len(lines):
            return acc + ["-1"]
        res = process_case(lines[idx], lines[idx+1])
        return process_input(idx+2, acc+[res], n-1)
    if not lines:
        return
    try:
        N = int(lines[0].strip())
    except:
        return
    results = process_input(1, [], N)
    print('\n'.join(results))

if __name__ == "__main__":
    main()
