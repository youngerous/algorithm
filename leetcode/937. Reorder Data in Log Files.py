class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # separate letter and digit logs
        letter, digit = [], []
        for log in logs:
            sublog = " ".join(log.split()[1:])
            if sublog[0].isalpha():
                letter.append(log)
            else:
                digit.append(log)

        # letter log sorting
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter + digit
