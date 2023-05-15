#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
* print_python_list_info - prints some basic info about pytohn list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = Py_SIZE(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, typeName);
    }
}
