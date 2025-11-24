# Análisis de Fracturas en Rocas - Guanajuato Capital

## Descripción del Proyecto


## Estructura del Proyecto

```
Proyecto-CdD/
│
├───data            # gestin de los datos
│   ├───cleaned     # datos preprocesados
│   └───raw         # datos originales
│
├───reports         # reporte de resultados y presentación
│   └───figures
└───src             # Código fuente principal
```

## Instalación y Configuración

### Prerrequisitos
```bash
# Clonar el repositorio
git clone https://github.com/HazelS002/Proyecto-CdD.git
cd Proyecto-CdD

# Crear entorno de Conda
conda env create -f environment.yml

# Activar entorno de Conda
conda activate data-science
```

### Dependencias
#### Dependencias principales

#### Dependencias secundarias



## Uso del Proyecto

### Ejecución del código fuente en SRC
```bash
# Ejecutar 
python -m src.<file-name>
```

**Funcionalidades en desarrollo:**
- 
- Controlar rutas desde un sólo archivo


## Estructura de Datos

### Formato de Entrada

## Desarrollo

### Agregar Nuevas Funcionalidades
1. Crear módulo en `src/` correspondiente
2. Actualizar `environment.yml` si es necesario

### Estructurar Nuevos Módulos
```python
# Ejemplo de estructura de módulo
nuevo_modulo/
├── __init__.py
├── . . .
└── helpers.py
```

## Contribución

1. Fork del proyecto
2. Crear rama feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crear Pull Request

## Mantenimiento

### Actualizar Dependencias
```bash
conda env update -f environment.yml --prune
```

### Compilar Reporte
```bash
# Generar reportes
cd reports/
pdflatex main.tex
```

## Contacto

- **Autor**: Hazel Shamed
- **Repositorio**: [github.com/HazelS002/Analisis-Fractura-Roca](https://github.com/HazelS002/Analisis-Fractura-Roca)
- **Institución**: Universidad de Guanajuato

---

*Este proyecto está en desarrollo activo. La estructura y funcionalidades pueden cambiar.*