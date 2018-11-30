
> #### Quick info:
>
> **Taller:** *Machine Learning as a Service (MLaaS): Sirvendo soluciones inteligentes* <br>
> **Tallerista:** Rodolfo Ferro <br>
> **Twitter:** [@FerroRodolfo](https://twitter.com/FerroRodolfo) <br>
> **Contacto:** [https://rodolfoferro.xyz](https://rodolfoferro.xyz) <br>
> **Slides:** [¡Click aquí!]()
------
![MLaaS](assets/MLaaS.png)

# Machine Learning as a Service (MLaaS): Sirvendo soluciones inteligentes

En este taller se creará un servicio que utilice algún modelo de aprendizaje de máquina entrenado, a través de una REST API. Todo ello con el poder de Keras, Tensorflow, NumPy, Pandas y Flask.

La idea será introducir lo que es MLaaS y entrenar una [*red neuronal*](https://es.wikipedia.org/wiki/Red_neuronal_artificial) para resolver algún problema específico utilizando Keras y Google Colab, tras esto, guardar los pesos entrenados para cargar la arquitectura de manera local y montar el sistema a través de una API construida con Flask.

Para este taller se necesitan conocimientos intermedio-avanzados sobre programación en Python, sobretodo con el uso de paquetería científica (NumPy, Pandas y de ser posible Flask y Keras). Parte de los objetivos es que posterior al taller se cuente con material y conocimientos para poder desarrollar modelos de IA como servicio; con Python, por supuesto. Para el taller se proporciona código base para a partir de ahí montar el servicio.

## ⚙️ Instalación

La versión más reciente de [Anaconda](https://www.anaconda.com/download/) (3.7) con [Python >= 3.6](https://www.python.org/downloads/) va a ser requerida. Trabajaremos utilizando un entorno de Anaconda para este taller.

Para crear el `conda env` e instalar los requerimientos sólo clona el repo:
```bash
# Clona el repo de GitHub:
git clone https://github.com/PythonDayMX/MLaaS.git
cd MLaaS
```

Y corre lo siguiente:
```bash
# Crea el entorno de Anaconda:
conda env create -f environment.yml
```

Para activar/desactivar el entorno:
```bash
# Activar entorno:
conda activate MLaaS

# Desactivar entorno:
conda deactivate
```

Para el entrenamiento del modelo de IA, estaremos trabajando en [Google Colab](https://colab.research.google.com/), donde puedes acceder a notebooks en línea para crear y entrenar modelos en la nube.

Puedes importar todos los notebooks directamente a Colab en la sección de GitHub a través del link a este repositorio: https://github.com/PythonDayMX/MLaaS

## 👾 Contenido

El repositorio y taller están autocontenidos, a través del notebook `MNIST - CNN Model.ipynb` dentro de la carpeta code que contiene todo el código a desarrollarse durante el taller, además de incluirse un modelo pre-entrenado y un conjunto de imágenes utilizadas en el notebook.


***

### SOBRE EL USO DE INFORMACIÓN TOTAL O PARCIAL: 🔐
* Estos documentos fueron originalmente creados por el autor.
* Cualquier uso de estos documentos o sus contenidos están permitidos a través de la licencia provista y sus condiciones.
* Para cualquier aclaración, puedes contactar al autor: https://rodolfoferro.xyz/

**Copyright (c) 2018 Rodolfo Ferro**
