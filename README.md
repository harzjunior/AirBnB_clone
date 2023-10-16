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
