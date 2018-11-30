
> #### Quick info:
>
> **Taller:** *Machine Learning as a Service (MLaaS): Sirvendo soluciones inteligentes*
> **Tallerista:** Rodolfo Ferro
> **Twitter:** [@FerroRodolfo](https://twitter.com/FerroRodolfo)
> **Contacto:** [https://rodolfoferro.xyz](https://rodolfoferro.xyz)
> **Slides:** [¡Click aquí!]()
------
![MLaaS](assets/MLaaS.png)

# Machine Learning as a Service (MLaaS): Sirvendo soluciones inteligentes

## 📑 Descripción

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
# Instala el entorno de Anaconda:
conda env create -f environment.yml
```

Para activar/desactivar el entorno:
```bash
# Activar entorno:
conda activate MLaaS

# Desactivar entorno:
conda deactivate
```

## 💻 Licencia
------
