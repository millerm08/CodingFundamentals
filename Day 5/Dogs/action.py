from dogclass import Dog
from policeDog import PoliceDog
from rescueDog import RescueDog
from PetDogClass import PetDog
from snifferDogClass import SnifferDog

dogs = [
    PoliceDog("Rookie", "Charles Xaviar"),
    RescueDog("Mountain Rescue", "Stan"),
    PetDog(33, "Kim", "Snoodle Terrier", 5),
    SnifferDog()
    ]



for dog in dogs:
    dog.run()
    dog.clean()
    try:
        dog.arrest()
    except:
        pass


