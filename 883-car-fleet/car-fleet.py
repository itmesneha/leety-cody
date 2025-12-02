class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        does not matter when the car collides 
        as long as it collides within the end target mile

        sort based on position.
        so if we go from back, find pairs of collisions (using stack).
        then combine them to slower speed.
        this way even if an earlier positioned car collided
        it will still be in the same fleet by the end (because it was moving faster anyway).

        time = O(nlogn)
        space = O(n)
        '''

        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target - p) / s) # time it reaches end
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)