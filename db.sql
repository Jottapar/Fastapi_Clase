-- ===========================
-- TABLAS CATÁLOGO
-- ===========================

CREATE TABLE roles (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP
);

CREATE TABLE acta (
  id SERIAL PRIMARY KEY,
  numero VARCHAR(7) NOT NULL,
  observaciones TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP
);

CREATE TABLE tareas_ope (
  id SERIAL PRIMARY KEY,
  tarea TEXT NOT NULL,
  estado VARCHAR(20),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP
);

CREATE TABLE insumos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(20) NOT NULL,
  tipo VARCHAR(20),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP
);

-- ===========================
-- TABLAS PRINCIPALES
-- ===========================

CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  doc_identidad VARCHAR(10) NOT NULL UNIQUE,
  nombre_completo VARCHAR(100) NOT NULL,
  celular VARCHAR(13) NOT NULL,
  correo VARCHAR(100) NOT NULL,
  contrasena VARCHAR(100) NOT NULL, -- ampliado para hash
  estado VARCHAR(15),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP,
  rol_id INT NOT NULL REFERENCES roles(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE ordenes_trabajo (
  id SERIAL PRIMARY KEY,
  fecha_creacion DATE NOT NULL,
  detalles TEXT,
  direccion VARCHAR(100) NOT NULL,
  fecha_ope TIMESTAMP NOT NULL,
  estado VARCHAR(20),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP,

  acta_id INT NOT NULL REFERENCES acta(id) ON UPDATE CASCADE ON DELETE RESTRICT,
  usuario_id INT NOT NULL REFERENCES usuarios(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE asignaciones_ordenes_trabajo (
  id SERIAL PRIMARY KEY,
  estado VARCHAR(20),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP,

  asignador_id INT NOT NULL REFERENCES usuarios(id) ON UPDATE CASCADE ON DELETE RESTRICT,
  orden_trabajo_id INT NOT NULL REFERENCES ordenes_trabajo(id) ON UPDATE CASCADE ON DELETE RESTRICT,
  tarea_id INT NOT NULL REFERENCES tareas_ope(id) ON UPDATE CASCADE ON DELETE RESTRICT,
  insumo_id INT NOT NULL REFERENCES insumos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
  asignado_id INT NOT NULL REFERENCES usuarios(id) ON UPDATE CASCADE ON DELETE RESTRICT
);
