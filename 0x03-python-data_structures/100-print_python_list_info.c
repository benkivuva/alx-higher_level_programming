#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @p: Pointer to a Python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = Py_SIZE(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated Memory = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;

		printf("Element %zd: %s\n", i, type);
	}
}
