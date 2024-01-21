from os import system
import os

system("cls")


# a = [1, 2, 3, 4]

# if (b := a)[0] == a[1]:
#     print(b[0])
#     print("its done")
#     print("b:", b)


# i = {"1": 2, "3": 4, "5": 6}

# for key, value in i.items():
#     print(value)


# controllers = {
#     "controller_1": "http://192.168.1.252/status.xml",
#     "controller_2": "http://192.168.1.252/status.xml",
#     "controller_3": "http://192.168.1.252/status.xml",
# }


# print(type(controllers.items()))
# print(list(controllers.items()).append([1, 1]))


# tup = (("a", "b", "c", "d", "e", "f"), ("aa", "bb", "cc", "dd", "ee", "ff"))

# for a, b, c, d, e, f, g in tup:
#     print(a)
#     print(type(a))


# if test := ([[]]):
#     print("yes")

# print(test)


# if test := 0:
#     print("yes")

# print(test)

# test = '<?xml version="1.0" encoding="windows-1252"?> <Monitor> <Device>TCW122B-CM</Device> <ID>5C:32:C5:00:B5:24</ID> <Hostname>TCW122B-CM     </Hostname> <FW>4.00</FW> <DigitalInput1Description>Digital 1</DigitalInput1Description> <DigitalInput1>OPEN</DigitalInput1> <DinAlarm1>0</DinAlarm1> <DigitalInput2Description>Digital 2</DigitalInput2Description> <DigitalInput2>OPEN</DigitalInput2> <DinAlarm2>0</DinAlarm2> <AnalogInput1Description>Analog 1</AnalogInput1Description> <AnalogInput1>0.0V</AnalogInput1> <AinAlarm1>0</AinAlarm1> <AnalogInput2Description>Analog 2</AnalogInput2Description> <AnalogInput2>0.0V</AnalogInput2> <AinAlarm2>0</AinAlarm2> <Sensor1Description>Sensor 1</Sensor1Description> <Temperature1>27.0&#176;C</Temperature1> <TempAlarm1>0</TempAlarm1> <Humidity1>23.2%RH</Humidity1> <HumAlarm1>0</HumAlarm1> <Sensor2Description>Sensor 2</Sensor2Description> <Temperature2>---</Temperature2> <TempAlarm2>0</TempAlarm2> <Humidity2>---</Humidity2> <HumAlarm2>0</HumAlarm2> <Relay1Description>Relay 1</Relay1Description> <Relay1>OFF</Relay1> <Relay1Control></Relay1Control> <Relay2Description>Relay 2</Relay2Description> <Relay2>OFF</Relay2> <Relay2Control></Relay2Control> <pulseWidth>1</pulseWidth> </Monitor>'


# a = 2


# def test():
# #     print("a")
# #     print("b")
# #     print("c")


# # test()


# dirname = os.path.dirname(__file__) + "\\{}"
# # dirname = os.path.dirname(__file__)
# print(dirname)
# print(type(dirname))


# str1 = "this is 1 thing"
# str1 = str1.replace("is 1 thing", "")

# print(str1)

# import sched, time


# def do_something(scheduler):
#     # schedule the next call first
#     scheduler.enter(5, 1, do_something, (scheduler,))
#     print("Doing stuff...")
#     # then do your stuff


# my_scheduler = sched.scheduler(time.time, time.sleep)
# print(type(my_scheduler))

# my_scheduler.enter(5, 1, do_something, (my_scheduler,))
# print(type(my_scheduler))

# my_scheduler.run()


# x = lambda a: a + 10
# print(x(5))

# print(x(5))


# print(x(333))


def test(i: str) -> "str":
    print(i + 3)
    return 0


test(9)

help(test)
