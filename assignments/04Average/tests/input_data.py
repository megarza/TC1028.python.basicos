# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["4", "3", "2"],
        # Outputs
        ["Dame un número: ", "Dame un número: ", "Dame un número: ", "El promedio de los números es: 3.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    ),
    (
        # Inputs
        ["2", "2", "2"],
        # Outputs
        ["Dame un número: ", "Dame un número: ", "Dame un número: ", "El promedio de los números es: 2.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores."
    )
]