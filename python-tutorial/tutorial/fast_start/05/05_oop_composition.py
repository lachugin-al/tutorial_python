# Композиция

class Engine:
    def on(self):
        print('on')

    def off(self):
        print('off')

class Stereo:
    def rock(self):
        print('rock')

class Car:
    __engine = Engine()
    stereo = Stereo()

    def start(self):
        print('let\'s start')
        self.__engine.on()
        self.stereo.rock()
    def stop(self):
        print('let\'s stop')
        self.__engine.off()
    def change_engine(self, new_engine: Engine):
        self.__engine = new_engine


auto = Car()
# auto.engine.on()
auto.start()
auto.stop()

engine2 = Engine()
auto.change_engine(engine2)
auto.start()