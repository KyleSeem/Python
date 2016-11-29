Assignment: Animal


1. Create a class called Animal with the following attributes:
    * name
    * health = 100

2. Give the animal following three methods:
    * walk = health decreases by 1
    * run = health decreases by 5
    * displayHealth = display name and health of the animal

3. Create an instance of the animal called 'animal' and have this animal do the following:
    * walk three times
    * run twice
    * displayHealth

4. Create another class called Dog that inherits everything from Animal, but:
    * default health is 150
    * add new method called getPets = increase the health by 5

5. Have the Dog do the following:
    * walk three times
    * run twice
    * getPets once
    * displayHealth

6. Create another class called Dragon that also inherits everything from Animal, but:
    * default health is 170
    * add new method called fly = decreases health by 10

7. Have the Dragon do the following:
    * walk three times
    * run twice
    * fly twice
    * displayHealth()

8. When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).

9. For the first instance of the animal (instance called 'animal'), call fly or getPets and make sure this doesn't work
