class Infos:
    def __init__(self):
        while True:
            try:
                self.height = float(input("Enter your height in centimeters: "))
                if self.height <= 0:
                    raise ValueError("Height must be a positive number")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        while True:
            try:
                self.distance = float(input("Enter distance you have walked today in kms: "))
                if self.distance < 0:
                    raise ValueError("Distance must be a non-negative number")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")


class Conversions(Infos):
    def convert_height(self):
        return self.height / 100

    def convert_distance(self):
        return self.distance * 1000


class StepsLength(Conversions):
    def calculate_step_length(self):
        height_in_meters = self.convert_height()
        self.step_length = 0.415 * height_in_meters
        return self.step_length


class StepsCalculator(StepsLength):
    def calculate_steps(self):
        try:
            self.distance_in_meters = self.convert_distance()
            self.step_length = self.calculate_step_length()
            number_of_steps = self.distance_in_meters / self.step_length
            print(f"Whoa! it's a huge, You have walked {self.distance} kms which sums up to {number_of_steps:.2f} steps")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please check your inputs.")
        except Exception as e:
            print(f"An error occurred: {e}")


steps = StepsCalculator()
steps.calculate_steps()