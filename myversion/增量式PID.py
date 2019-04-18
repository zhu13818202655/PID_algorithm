class PID:
    def __init__(self, speed):
        self.SetSpeed = speed
        self.ActualSpeed = 0.0
        self.err = 0.0
        self.nexterr = 0.0
        self.lasterr = 0.0
        self.Kp = 0.2
        self.Ki = 0.015
        self.Kd = 0.2

    def PID_realize(self):
        self.err=self.SetSpeed - self.ActualSpeed

        self.incrementSpeed = self.Kp*(self.err-self.nexterr)+self.Ki*self.err+self.Kd*(self.err-2*self.nexterr+self.lasterr)
        self.ActualSpeed += self.incrementSpeed
        self.lasterr = self.nexterr
        self.nexterr = self.err
        return self.ActualSpeed

if __name__ == '__main__':

    print("System begin")
    count = 0
    speed = PID(200.0)
    while count < 1000:

        ActualSpeed = speed.PID_realize()
        count += 1
    while count < 2000:

        ActualSpeed = speed.PID_realize()
        count += 1
    print(ActualSpeed)
    print("System over")


