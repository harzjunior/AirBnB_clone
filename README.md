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

