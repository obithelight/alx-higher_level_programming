# 0x05. Python - Exceptions

## Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone:

### Why Python Programming is Awesome:
- Readability: Python has a clean and readable syntax that makes it easy to learn and write code.
- Versatility: Python is a versatile language suitable for various applications, including web development, data science, machine learning, automation, and more.
- Large Standard Library: Python comes with a comprehensive standard library, providing modules and packages for a wide range of tasks.
- Community Support: Python has a large and active community, which means abundant resources, libraries, and frameworks, as well as a wealth of online tutorials and forums for support.
- Cross-Platform: Python is platform-independent, making it easy to write code that can run on different operating systems without modification.

### Difference Between Errors and Exceptions:
- Errors: Errors in Python are problems that occur at runtime and terminate the program. They are generally more severe and harder to recover from.

- Exceptions: Exceptions are events that occur during the execution of a program but are not necessarily fatal. Python provides a way to handle these exceptions and continue the program's execution.

### What are Exceptions and How to Use Them:
- Exceptions: Exceptions are events that disrupt the normal flow of a program's instructions when an error or unexpected condition occurs.

- How to Use Them: You can use the try, except, else, and finally blocks to handle exceptions. The code inside the try block is executed, and if an exception occurs, the corresponding except block is executed.

- When to Use Exceptions:
Use Exceptions When:
	Dealing with situations where errors are expected and can be handled gracefully.
	Avoiding abrupt program termination due to errors.
	Providing a clear separation between error-handling code and normal code.

### How to Correctly Handle an Exception:
- Use try, except, and optionally else and finally blocks.
- Handle specific exceptions if possible, and avoid catching generic Exception unless necessary.
- Keep the try block as small as possible to precisely identify the potential source of an exception.

### Purpose of Catching Exceptions:
- Preventing Program Termination: Catching exceptions allows a program to continue execution even when errors occur.
Error Logging: Catching exceptions facilitates error logging, helping developers identify and troubleshoot issues.

### How to Raise a Built-in Exception:
- Use the `raise` statement, followed by the exception type. For example: 
`raise ValueError("This is a custom error message.")`

### When to Implement a Clean-Up Action After an Exception:
- Use the `finally` block to implement clean-up actions that must be executed regardless of whether an exception occurs.
- Common use cases include closing files, releasing resources, or cleaning up temporary data.
