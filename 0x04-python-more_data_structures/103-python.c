#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_bytes - prints info about python bytes objects
 * @p: address of PyObject struct
 */
void print_python_bytes(PyObject *p)
{
	if (p == NULL)
	{
		printf("NULL\n");
	}

	if (PyBytes_Check(p))
	{
		Py_ssize_t len = PyBytes_Size(p);
		printf("Bytes object of length %zu:\n", len);
		char *bytes = PyBytes_AsString(p);
		if (bytes == NULL)
		{
			printf("Unable to read bytes object\n");
			return;
		}
		for (Py_ssize_t i = 0; i < len; i++)
		{
			printf("%c", bytes[i]);
		}
		printf("\n");
	}
	else
	{
		printf("Not a bytes object\n");
	}
}

/**
 * print_python_list - prints info about python lists
 * @p: address of PyObject struct
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Not a list\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = item->ob_type->tp_name;
		printf("Element %zd: %s\n", i, typeName);
	}
}
