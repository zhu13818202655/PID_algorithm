class PID:
    def __init__(self, speed):
        self.SetSpeed = speed
        self.ActualSpeed = 0.0
        self.err = 0.0
        self.lasterr = 0.0
        self.Kp = 0.2
        self.Ki = 0.015
        self.Kd = 0.2
        self.voltage = 0.0
        self.integral = 0.0

    def PID_realize(self):
        self.err=self.SetSpeed - self.ActualSpeed
        self.integral += self.err
        self.voltage = self.Kp*self.err+self.Ki*self.integral+self.Kd*(self.err-self.lasterr)
        self.lasterr = self.err
        self.ActualSpeed = self.voltage*1.0
        return self.ActualSpeed

if __name__ == '__main__':

    print("System begin")
    count = 0
    speed = PID(200.0)
    while count < 1000:

        ActualSpeed = speed.PID_realize()
        count += 1

    print(ActualSpeed)
    print("System over")


