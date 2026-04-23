from math import sin, cos, pow, radians


#Parent Class
class Projectile:
    def __init__(self, velocity, angle, time_interval=0.05, gravity=9.81):
        self.velocity = velocity
        self.angle = radians(angle)
        self.time_interval = time_interval
        self.gravity = gravity
        self.x_coordinates = []
        self.y_coordinates = []

    def get_coordinates(self):
        time = 0
        while True:
            x = self.velocity * cos(self.angle) * time
            y = (self.velocity * sin(self.angle) * time) - (0.5 * self.gravity * pow(time, 2))
            if y < 0:
                break
            self.x_coordinates.append(round(x,7))
            self.y_coordinates.append(round(y,7))
            time += self.time_interval


#Subclass of Parent Class: Inheriting all instance variables of class Projectile
class Ground2GroundMetrics(Projectile):
    def __init__(self, velocity, angle, time_interval=0.05, gravity=9.81):
        super().__init__(velocity,angle, time_interval, gravity)

    def get_max_height(self):
        return round((pow(self.velocity, 2) * pow(sin(self.angle), 2)) / (2*self.gravity), 3)

    def get_time_flight(self):
        return round((2 * self.velocity * sin(self.angle)) / self.gravity, 3)

    def get_range(self):
        return round((pow(self.velocity, 2) * sin(2 * self.angle)) / self.gravity, 3)

    def results(self):
        return [f"1. Projectile Max Height: {Ground2GroundMetrics.get_max_height(self)} meters",
                f"2. Projectile Range: {Ground2GroundMetrics.get_range(self)} meters",
                f"3. Time Of Flight: {Ground2GroundMetrics.get_time_flight(self)} seconds \n"
                ]

class Height2GroundMetrics(Projectile):
    def __init__(self, velocity, angle, height, time_interval=0.05, gravity=9.81):
        super().__init__(velocity,angle, time_interval, gravity)
        self.height = height

    def get_coordinates(self):
        time = 0
        while True:
            x = self.velocity * cos(self.angle) * time
            y = (0.5 * self.gravity * pow(time, 2)) - (self.velocity * sin(self.angle) * time) - self.height
            if y > 0:
                break

            self.y_coordinates.append(round(-y,7))
            self.x_coordinates.append(round(x,7))
            time += self.time_interval

    def get_time_flight(self):
        return round((self.velocity*sin(self.angle) + pow(pow(self.velocity*sin(self.angle), 2) + (4*self.height*0.5*self.gravity),0.5))/self.gravity, 3)

    def get_range(self):
        return round(self.velocity*cos(self.angle)*Height2GroundMetrics.get_time_flight(self), 3)

    def get_max_height(self):
        return round(((pow(self.velocity*sin(self.angle), 2)) / (2*self.gravity))   + self.height, 3)

    def results(self):
        return [f"1. Projectile Max Height: {Height2GroundMetrics.get_max_height(self)} meters",
                f"2. Projectile Range: {Height2GroundMetrics.get_range(self)} meters",
                f"3. Time Of Flight: {Height2GroundMetrics.get_time_flight(self)} seconds \n"
                ]


def main():
    ...


if __name__ == "__main__":
    main()

