from rubberduck import RubberDuck

duck = RubberDuck()
print(duck)  # שימוש ב-__str__

RubberDuck.squeak()

duck.quack_volume = 10
print("🔊 New volume:", duck.quack_volume)

duck.boost_volume()
print("🚀 Boosted volume:", duck.quack_volume)

print("🎨 Default color:", RubberDuck.get_color())