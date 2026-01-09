import nbformat

nb = nbformat.read("SOTA_Task_3_5.ipynb", as_version=4)

# Remove only broken widget metadata
nb.metadata.pop("widgets", None)

nbformat.write(nb, "SOTA_Task_3.ipynb")