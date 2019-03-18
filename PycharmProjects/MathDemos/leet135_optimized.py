class Solution:

    def candy(self, ratings) -> int:
        if len(ratings) == 0:
            return 0

        if len(ratings) == 1:
            return 1

        mode = ''  # 'increasing' , 'decreasing' , 'constant'
        start = 0
        finish = 1
        candies_amount = []

        if ratings[start] < ratings[finish]:
            mode = 'increasing'
        elif ratings[start] > ratings[finish]:
            mode = 'decreasing'
        elif ratings[start] == ratings[finish]:
            mode = 'constant'

        for i in range(2, len(ratings)):
            prev = ratings[i - 1]
            curr = ratings[i]
            if mode == 'increasing':
                if prev < curr:

                    pass
                elif prev > curr:
                    pass
                elif prev == curr:
                    pass
                pass
            elif mode == 'decreasing':
                pass
            elif mode == 'constant':
                pass

