# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/submissions/1634941131/

def numberOfSubstrings(s: str) -> int:
        n = len(s)
        
        # 1. Build a list of zero positions, with sentinels at -1 and n
        zero_pos = [-1]              # sentinel before the string
        for i, ch in enumerate(s):   # enumerate gives (index, char)
            if ch == '0':
                zero_pos.append(i)
        zero_pos.append(n)           # sentinel after the string

        result = 0

        # 2. k = 0 case: pure‑ones runs
        #    Between zero_pos[i] and zero_pos[i+1] you have L = gap length of 1's
        #    Each run of L ones yields L*(L+1)//2 substrings
        for i in range(len(zero_pos) - 1):
            L = zero_pos[i+1] - zero_pos[i] - 1
            if L > 0:
                result += L * (L + 1) // 2

        # 3. For k >= 1 zeros, only try up to sqrt(n)
        max_k = int(math.sqrt(n))
        for k in range(1, max_k + 1):
            # minimal length of substring with k zeros = k + k^2
            min_len = k + k*k

            # slide a block of k zeros over zero_pos
            # window covers zeros at zero_pos[i] ... zero_pos[i+k-1]
            for i in range(1, len(zero_pos) - k):
                first_zero = zero_pos[i]
                last_zero  = zero_pos[i + k - 1]

                # any start can be from (prev_zero+1) to first_zero
                start_min = zero_pos[i-1] + 1
                start_max = first_zero

                # any end can be from last_zero to (next_zero-1)
                end_min = last_zero
                end_max = zero_pos[i + k] - 1

                # for each possible start, find how many ends keep length >= min_len
                for start in range(start_min, start_max + 1):
                    # substring must be long enough *and* must reach the last zero
                    need_end = max(start + min_len - 1, last_zero)
                    if need_end > end_max:
                        # no more valid ends for larger starts either
                        break
                    # all ends from need_end up to end_max work
                    result += end_max - need_end + 1

        return result