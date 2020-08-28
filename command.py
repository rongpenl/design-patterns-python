from abc import ABC, abstractmethod
from enum import Enum


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        print("No comand")

    def undo(self):
        print("No command")


class OnCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class OffCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class Appliance(ABC):
    def __init__(self, description: str):
        self._description = description

    def __repr__(self):
        return self._description


class Light(Appliance):
    def on(self):
        print("{} Light on".format(self._description))

    def off(self):
        print("{} Light off".format(self._description))


class LightOnCommand(OnCommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(OnCommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GarageDoor(Appliance):
    def up(self):
        print("{} Door up".format(self._description))

    def down(self):
        print("{} Door down".format(self._description))


class GarageDoorUpCommand(OnCommand):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorDownCommand(OnCommand):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()


class FanSpeed(Enum):
    Low = 0
    Medium = 1
    High = 2
    OFF = 3


class CeilingFan(Appliance):
    def __init__(self, description: str):
        self._description = description
        self.SPEED = FanSpeed
        self._speed = self.SPEED.OFF

    def get_speed(self):
        return self._speed

    def change(self, direction: int = 1):
        self._previous_state = self.get_speed()
        val = self._speed.value
        new_val = (val + direction) % len(self.SPEED)
        self._speed = self.SPEED(new_val)
        print("Changing speed from {} to {}".format(
            self.SPEED(val), self.SPEED(new_val)))


class CeilingFanCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self._previous_state = ceiling_fan.get_speed()
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.change()

    def undo(self):
        self.ceiling_fan.change(-1)


class RemoteControl():

    def __init__(self):
        self.num_slot = 7
        self.on_commands = [NoCommand() for _ in range(self.num_slot)]
        self.off_commands = [NoCommand() for _ in range(self.num_slot)]
        self.undo_command = NoCommand()

    def set_command(self, slot: int, on_command: OnCommand,
                    off_command: OffCommand):
        if slot >= self.num_slot:
            print("Unable to set command.")
            return
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def press_on_button(self, slot: int):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def press_off_button(self, slot: int):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def press_undo_button(self):
        self.undo_command.undo()

    def __repr__(self):
        return "Remote control"


if __name__ == "__main__":
    light1 = Light("Livingroom")
    light2 = Light("Kitchen")

    door1 = GarageDoor("Front")
    door2 = GarageDoor("Back")

    fan1 = CeilingFan("Livingroom")
    fan2 = CeilingFan("Kitchen")

    light1_on_command = LightOnCommand(light1)
    light2_on_command = LightOnCommand(light2)
    light1_off_command = LightOffCommand(light1)
    light2_off_command = LightOffCommand(light2)

    door1_up_command = GarageDoorUpCommand(door1)
    door2_up_command = GarageDoorUpCommand(door2)
    door1_down_command = GarageDoorDownCommand(door1)
    door2_down_command = GarageDoorDownCommand(door2)

    fan1_command = CeilingFanCommand(fan1)
    fan2_command = CeilingFanCommand(fan2)

    remote_control = RemoteControl()

    remote_control.set_command(0, light1_on_command, light1_off_command)
    remote_control.set_command(1, light2_on_command, light2_off_command)
    remote_control.set_command(2, door1_up_command, door1_down_command)
    remote_control.set_command(3, door2_up_command, door2_down_command)

    # set fan button
    remote_control.set_command(4, fan1_command, NoCommand())
    remote_control.set_command(5, fan2_command, NoCommand())

    # next line will fail
    remote_control.set_command(7, door2_up_command, door2_down_command)

    for i in range(6):
        remote_control.press_on_button(4)
    remote_control.press_undo_button()

'''
Encapsulate classes with a command class and pass command object to client
or further encapsulate (into remote control, for example).
'''
