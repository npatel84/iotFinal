import subprocess

class Light:
    def __init__(self, name=""):
        self.status = "on"
        self.name = name

    def switch(self, value):
        result = f"{self.name} switched "
        if value == "on":
            # Run bash script on
            print(subprocess.run(["/home/pi/kasa-light.sh on"], shell=True))
            result = result + "on"
        if value == "off":
            # Run bash script off
            print(subprocess.run(["/home/pi/kasa-light.sh off"], shell=True))
            result = result + "off"
        return result
