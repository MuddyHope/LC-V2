class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for car_pos, car_speed in cars:

            time = (target - car_pos) / car_speed

            stack.append(time)


            # Merge fleets
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()


        return len(stack)