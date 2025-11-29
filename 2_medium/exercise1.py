# Mode:Medium , Exercise 1
"""
Exercise 1
Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
Input : [-1,0,1,2,-1,-4] Output : [[-1, -1, 2], [-1, 0, 1]] Note : Find the unique triplets in the array.
"""
def find_zero_sum_triplets(a: list):
    # ---------------------------------------------------------------
    # 1. SORTING THE ARRAY
    # ---------------------------------------------------------------
    # Sorting is absolutely necessary for the two-pointer technique.
    # After sorting:
    # - All duplicates sit next to each other (important for skipping).
    # - If we move 'left' pointer to the right → numbers become larger.
    # - If we move 'right' pointer to the left → numbers become smaller.
    # This allows us to adjust the sum in a controlled, predictable way.
    # ---------------------------------------------------------------
    a.sort()
    print("Sorted array:", a)

    # This will hold all the VALID and UNIQUE triplets we find.
    result = []

    # ---------------------------------------------------------------
    # 2. MAIN LOOP: Fix the first number of the triplet (a[i])
    # ---------------------------------------------------------------
    # i goes from the first element to the 3rd last element.
    # Why to the 3rd last? Because we need at least two numbers after i
    # for left and right pointers.
    # ---------------------------------------------------------------
    for i in range(len(a)):

        # -----------------------------------------------------------
        # SKIP DUPLICATE VALUES FOR i
        # -----------------------------------------------------------
        # Important: If a[i] is the same as a[i-1], we already processed
        # the combinations that begin with that number. Using it again
        # would only create duplicate triplets.
        #
        # Example:
        # If a = [-1, -1, ...]
        # Then when i = 1, the number is -1 again → skip it.
        # -----------------------------------------------------------
        if i > 0 and a[i] == a[i - 1]:
            continue

        # -----------------------------------------------------------
        # 3. INITIALIZE TWO POINTERS FOR EACH i:
        # left  → the element immediately after i
        # right → the last element of the array
        #
        # These two pointers will explore all possible pairs (left,right)
        # that can combine with a[i] to sum to 0.
        # -----------------------------------------------------------
        left = i + 1
        right = len(a) - 1

        # -----------------------------------------------------------
        # 4. TWO-POINTER SEARCH
        # -----------------------------------------------------------
        # As long as left is before right, there are still combinations
        # to test. When left ≥ right, no combinations remain.
        # -----------------------------------------------------------
        while left < right:

            # Compute the sum of the current triplet candidate:
            #   a[i]    = fixed number
            #   a[left] = growing number (as left increases)
            #   a[right]= shrinking number (as right decreases)
            s = a[i] + a[left] + a[right]

            # -------------------------------------------------------
            # CASE 1: Perfect match → the triplet sums to 0
            # -------------------------------------------------------
            if s == 0:
                # Save the triplet
                result.append([a[i], a[left], a[right]])

                # ---------------------------------------------------
                # SKIP DUPLICATES FOR LEFT POINTER
                # ---------------------------------------------------
                # Because the array is sorted, duplicates appear next
                # to each other. If a[left] == a[left+1], then using
                # left+1 would create the SAME triplet again.
                #
                # Example:
                #   [-1, -1, -1, 2]
                # left=1 → -1
                # left=2 → -1 ← duplicate!
                #
                # We skip all such duplicates by advancing left until
                # the next value is *different*.
                # ---------------------------------------------------
                while left < right and a[left] == a[left + 1]:
                    left += 1

                # ---------------------------------------------------
                # SKIP DUPLICATES FOR RIGHT POINTER
                # ---------------------------------------------------
                # Same logic: if a[right] == a[right-1], we skip the
                # duplicate to avoid repeating the same triplet.
                # ---------------------------------------------------
                while left < right and a[right] == a[right - 1]:
                    right -= 1

                # ---------------------------------------------------
                # MOVE BOTH POINTERS AFTER FINDING A VALID TRIPLET
                # ---------------------------------------------------
                # Because:
                # - Using the current left/right again is pointless
                # - We want NEW combinations
                #
                # So we move left forward and right backward.
                # ---------------------------------------------------
                left += 1
                right -= 1

            # -------------------------------------------------------
            # CASE 2: Sum is too small (< 0)
            # -------------------------------------------------------
            # Because array is sorted:
            # → Increasing left moves to a larger number
            # → A larger number increases the total sum
            # -------------------------------------------------------
            elif s < 0:
                left += 1

            # -------------------------------------------------------
            # CASE 3: Sum is too big (> 0)
            # -------------------------------------------------------
            # Because array is sorted:
            # → Decreasing right moves to a smaller number
            # → A smaller number decreases the total sum
            # -------------------------------------------------------
            else:
                right -= 1

    # ---------------------------------------------------------------
    # After finishing all loops and pointer searches, return the result
    # ---------------------------------------------------------------
    return result



# ---------------------------------------------------------------
# TESTING THE FUNCTION
# ---------------------------------------------------------------
if __name__ == "__main__":
    a =  [-1,0,1,2,-1,-4]

    res = find_zero_sum_triplets(a)
    print("Resulting triplets:", res)
