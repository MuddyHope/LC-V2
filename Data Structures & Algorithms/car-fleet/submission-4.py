class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for car_pos, car_speed in cars:

            time = (target - car_pos) / car_speed



            # Merge fleets
            if not stack or stack[-1] < time:
                stack.append(time)


        return len(stack)