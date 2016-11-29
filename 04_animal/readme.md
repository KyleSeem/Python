Assignment: Animal

1. Create a class called Animal with the following attributes:
    a. name
    b. health
      * new instances get health of 100

2. Give the animal following three methods:
    a. walk
      * health decreases by 1
    b. run
      * health decreases by 5
    c. displayHealth
      * display name and health of the animal

3. Create an instance of the animal called 'animal' and have this animal do the following:
    a. walk three times
    b. run twice
    c. displayHealth

4. Create another class called Dog that inherits everything from Animal, but:
    a. default health is 150
    b. add a new method called getPets
        * increase the health by 5

5. Have the Dog do the following:
    a. walk three times
    b. run twice
    c. getPets once,
    d. displayHealth

6. Create another class called Dragon that also inherits everything from Animal, but:
    a. default health is 170
    b. add a new method called fly
      * decreases health by 10

7. Have the Dragon do the following:
    a. walk three times
    b. run twice
    c. fly twice
    d. displayHealth()

8. When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).

Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-:
