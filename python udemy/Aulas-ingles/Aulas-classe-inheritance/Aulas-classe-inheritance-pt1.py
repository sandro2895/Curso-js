class Device:
    def __init__(self, name, conected_by):
        self.name = name
        self.conected_by = conected_by
        self.conected = True

    def __str__(self):
        return f'Device: {self.name!r} ({self.conected_by})'


    def disconect(self):
        self.conected = False
        print('Disconnected')


class Printer(Device):
    def __init__(self, name, conected_by, capacity):
        super().__init__(name, conected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages}) pages remaining.'

    def printing(self, pages):
        if not self.conected:
            print('Your printer is not conected')
            return
        print(f'Printing {pages} pages.')
        self.remaining_pages -= pages


printer = Printer("Printer", 'USB', 20)
printer.printing(15)
print(printer)
printer.disconect()
printer.printing(2)0