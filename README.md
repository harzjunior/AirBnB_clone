# AirBnB Clone

## Step One: Developing a Command Interpreter for Managing AirBnB Objects

This marks the initial phase in constructing your inaugural web application, the AirBnB clone. This preliminary step carries immense significance as it sets the foundation for all forthcoming projects in the series, such as HTML/CSS templating, database storage, API development, and front-end integration.

Each task within this phase is intricately connected and contributes to the following objectives:

* Establish a parent class named [BaseModel] responsible for the initialization, serialization, and deserialization of your future instances.
* Create a straightforward process for serialization and deserialization: Instance ↔ Dictionary ↔ JSON string ↔ file.
* Develop all the classes necessary for the AirBnB application (e.g., [User, State, City, Place...]) that inherit from the [BaseModel] class.
* Implement the initial abstracted storage engine for the project, known as File storage.
* Create comprehensive unit tests to validate all our classes and the storage engine's functionality.

## Understanding a Command Interpreter

Have you ever used a Shell? Well, a command interpreter is similar, but it's tailored to a specific purpose. In our context, we aim to create a tool for effectively managing the components of our project.

With this command interpreter, you can perform the following key tasks:

* **Create a new object:** For example, you can generate a new User or a new Place in the context of our project.
* **Retrieve an object:** Whether it's stored in a file, a database, or elsewhere, you can retrieve an object.
* **Perform operations on objects:** This includes actions like counting objects, computing statistics, and more.
* **Update object attributes:** You have the ability to modify the attributes of an object as needed.
* **Destroy an object:** When it's time to remove an object, you can do so.

Moreover, it's essential to ensure that all tests are not only functional in interactive mode but also in non-interactive mode. You can achieve this by running the following command:

```bash
$ "python3 -m unittest discover tests" | bash
```

This command ensures that all your tests are executed successfully, even when not interacting directly with the interpreter.

## Execution

Your shell should function in both interactive and non-interactive modes. Here's how it should work:

**Interactive Mode:**
```bash
$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  nothing  quit  show  update

(hbnb)
(hbnb) 
(hbnb)quit
$ 
```

**Non-Interactive Mode (Similar to the Shell Project in C):**
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  nothing  quit  show  update
(hbnb) 
$
```

It's essential to ensure that all tests pass successfully in non-interactive mode as well:

```bash
$ echo "python3 -m unittest discover tests" | bash
```
```
.......
----------------------------------------------------------------------
Ran 52 tests in 0.021s

OK
```
## Tasks

## 0. README, AUTHORS [README.md, AUTHORS]
* Write a comprehensive README.md, which includes:
  * A project description.
  * An explanation of the command interpreter, covering how to start and use it.
* Create an AUTHORS file at the root of your repository, listing all individuals who have contributed content to the project. You can reference the format used in [Docker's AUTHORS page](https://github.com/moby/moby/blob/master/AUTHORS).
* Utilize branches and pull requests on GitHub to facilitate efficient team collaboration and organization.

## 1. Be PEP8 compliant! [ ...]
* Ensure that your code adheres to the PEP8 style guidelines, promoting clean and readable code.

## 2. Unittests [tests/]
* Implement unit tests for all your files, classes, and functions.
* Verify that your unit tests pass both in interactive mode and non-interactive mode using the following command:
  ```
  python3 -m unittest discover tests
  ```
  ```
  echo "python3 -m unittest discover tests" | bash
  ```

These tasks encompass project documentation, code quality, and comprehensive testing to ensure the robustness of your command interpreter.

This demonstrates that your shell can handle both interactive and non-interactive input and is capable of executing all the required commands effectively.

## 3. BaseModel

In the context of the `models/base_model.py` module and its associated components, we are tasked with creating a class named `BaseModel`. This class will serve as the foundation for all other classes in the project and will define common attributes and methods that will be shared across various objects.

Here's an outline of the key attributes and methods for the `BaseModel` class:

### Public Instance Attributes:

* `id` (string): An attribute that is assigned a universally unique identifier (UUID) when an instance is created. You can generate a unique ID using `uuid.uuid4()` and then convert it to a string. The objective is to ensure that each `BaseModel` instance has a unique ID.

* `created_at` (datetime): This attribute is assigned the current date and time when an instance is created.

* `updated_at` (datetime): Similar to `created_at`, this attribute is assigned the current date and time when an instance is created, and it is updated every time the object is modified.

### Public Instance Methods:

* `__str__(self)`: This method defines how an instance should be represented as a string. It should print in the following format: `[<class name>] (<self.id>) <self.__dict__>`. This is a human-readable representation of the object.

* `save(self)`: This method is responsible for updating the public instance attribute `updated_at` with the current date and time when it is called. It signifies that the object has been modified.

* `to_dict(self)`: This method returns a dictionary containing all the keys and values of the instance's `__dict__`. It ensures that only instance attributes set will be included in the dictionary. Additionally, a key called `__class__` must be added to this dictionary, indicating the class name of the object. The `created_at` and `updated_at` attributes must be converted to string objects in ISO format (e.g., "2017-06-14T22:31:03.285259"). This method serves as the first step in the serialization and deserialization process, creating a dictionary representation of the `BaseModel` object.

The `BaseModel` class and these methods will be fundamental for implementing the serialization/deserialization process for all objects within your project.

You will have a comprehensive web application, consisting of the following components:

1. **Command Interpreter**: This serves as a tool to manage data without the need for a visual interface, similar to working in a Shell. It's particularly valuable during the development and debugging phases.

2. **Website (Front-end)**: The web application includes a website that presents the final product to users. This website combines both static and dynamic elements to create an interactive user experience.

3. **Database or Files**: Your application relies on either a database or files to store data. In this context, data refers to objects relevant to the application's functionality.

4. **API (Application Programming Interface)**: The API functions as a communication interface between the front-end and your data storage. It enables operations such as retrieving, creating, deleting, and updating data, facilitating seamless interaction between the user interface and your data storage.

The final comment appears to reference running tests using `./test_base_model.py`. This command likely runs tests for the Base Model class or module to ensure its functionality. This is an essential part of maintaining the application's robustness and stability.

## 4. Create BaseModel from dictionary

In this step, we aim to recreate an instance of the `BaseModel` class from a dictionary representation. This is the reverse process of the `to_dict()` method we implemented earlier.

Here's the expected flow:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

The objective is to ensure that we can create a `BaseModel` instance using the dictionary representation we obtain from the `to_dict()` method. A test suite has been prepared to validate this functionality.

## 5. Store first object

Building on the previous step, we are now able to recreate a `BaseModel` from another one by using a dictionary representation. This means that we can store, serialize, and deserialize a `BaseModel` instance. The entire flow of serialization and deserialization is as follows:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```

In summary, the process involves converting a `BaseModel` instance to a dictionary, serializing it to JSON, saving it to a file, loading it from the file, deserializing the JSON, and reconstructing a `BaseModel` instance.

A test suite, `test_save_reload_base_model.py`, is provided to ensure the correct implementation of this functionality.

## 6. Console 0.0.1

In this step, you are required to create a program called `console.py` that serves as the entry point for the command interpreter. This console will allow you to interact with your project through various commands.

The specifications for this console are as follows:

* You must use the `cmd` module.
* Your class definition should be `class HBNBCommand(cmd.Cmd)`.
* The command interpreter should implement the following commands:
  * `quit` and `EOF` to exit the program.
  * `help` (provided by default by `cmd`, but you should keep it updated and documented as you work through tasks).
* The custom prompt should be `(hbnb)`.
* An empty line followed by pressing `ENTER` should not execute any commands.
* Your code should not be executed when imported.

The example usage provided demonstrates how the console should work, including the use of the `help` command and the custom prompt `(hbnb)`.

Once implemented, your console will become the primary interface for interacting with the project, allowing you to issue commands and perform various actions within the application.

## 7. Console 0.1

In this section, we are enhancing the functionality of the command interpreter, `console.py`, with various commands for managing different types of objects in our project. These commands include `create`, `show`, `destroy`, `all`, `update`, and they are applied to different classes.

Here's a summary of the updates to the command interpreter:

1. **create**: This command creates a new instance of a specified class, saves it to the JSON file, and prints its ID. If the class name is missing, it will print "**class name missing**." If the class name doesn't exist, it will print "**class doesn't exist**."

2. **show**: The `show` command prints the string representation of an instance based on the class name and ID. If any part of the input is missing or if the instance does not exist, appropriate error messages are printed.

3. **destroy**: This command deletes an instance based on the class name and ID, saving the change to the JSON file. It also handles various error scenarios, including missing class name, non-existent class name, missing ID, and non-existent instance.

4. **all**: The `all` command prints the string representation of all instances based on the class name. The printed result is a list of strings. It handles cases where the class name is missing or does not exist.

5. **update**: The `update` command updates an instance based on the class name and ID by adding or updating attributes and saving the changes to the JSON file. The usage format is `update <class name> <ID> <attribute name> "<attribute value>"`. It provides error messages for missing or non-existent class name, missing ID, missing attribute name, missing value, and disallows certain arguments.

These commands are now part of the console's functionality and can be used to manipulate various objects within the project.

## 8. First User

In this step, a new class called `User` is created, which inherits from `BaseModel`. The `User` class is defined in the `models/user.py` module. It includes public class attributes such as `email`, `password`, `first_name`, and `last_name`, all initialized with empty strings.

Additionally, the `console.py` command interpreter is updated to allow `show`, `create`, `destroy`, `update`, and `all` commands to be used with the `User` class.

## 9. More classes!

This step involves the creation of multiple classes, each of which inherits from `BaseModel`. The classes and their public class attributes include:

* `State` (models/state.py): It has a public class attribute `name`, initialized with an empty string.

* `City` (models/city.py): Public class attributes include `state_id` (initialized as an empty string, representing the State's ID) and `name` (an empty string).

* `Amenity` (models/amenity.py): It has a single public class attribute, `name`, initialized as an empty string.

* `Place` (models/place.py): This class includes several public class attributes: `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, and `amenity_ids`. Each attribute is initialized with appropriate default values.

* `Review` (models/review.py): It includes public class attributes `place_id`, `user_id`, and `text`, all initialized as empty strings.

## 10. Console 1.0

The Console, represented by the `console.py` module, is updated to work with the newly created classes. The `FileStorage` class is also enhanced to manage the serialization and deserialization of all the new classes: `Place`, `State`, `City`, `Amenity`, and `Review`.

The command interpreter is updated to allow commands like `show`, `create`, `destroy`, `update`, and `all` to be used with all classes created previously, including the new ones.

## 11. All instances by class name

The command interpreter is updated to include the ability to retrieve all instances of a class using `<class name>.all()`.

## 12. Count instances

The command interpreter is updated to include the ability to count the number of instances of a class using `<class name>.count()`.

## 13. Show

The `console.py` interpreter is further updated to retrieve an instance based on its ID using `<class name>.show(<id>)`. It handles errors in a similar fashion to previous commands.

## 14. Destroy

The `console.py` interpreter now includes a `destroy` command to delete an instance based on its ID using `<class name>.destroy(<id>)`. It handles errors in a similar fashion to previous commands.

## 15. Update

The command interpreter is updated to include the `update` command. It can update an instance based on its ID, an attribute name, and an attribute value using `<class name>.update(<id>, <attribute name>, <attribute value>)`. It handles errors similarly to previous commands, disallowing certain arguments.

## 16. Update from dictionary

The `console.py` interpreter is updated to support updating an instance based on its ID with a dictionary representation using `<class name>.update(<id>, <dictionary representation>)`. It handles errors similarly to previous commands.

## 17. Update Using a Dictionary [ tests/test_console.py ]

Contributors:
1. Haruna Bah

In this task, we will work on updating instances using a dictionary with attributes such as 'first_name' and 'age'. The provided test `test_console.py` demonstrates this functionality.
