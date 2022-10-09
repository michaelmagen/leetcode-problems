class Solution:
    def capitalizeTitle(self, title: str) -> str:
        answer = []
        # iterate through words in title
        for n in title.split():
            if len(n) < 3:
                # change all letter to lower
                answer.append(n.lower())
            else:
                # capitalize first letter and lower case the rest
                answer.append(n.capitalize())
        # return full string
        return " ".join(answer)