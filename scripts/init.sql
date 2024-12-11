CREATE DATABASE IF NOT EXISTS meme_app CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE meme_app;

CREATE TABLE memes (
    id CHAR(36) PRIMARY KEY,
    descripcion TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
    ruta TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
    usuario TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
    cargada TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE etiquetas (
    id CHAR(36) PRIMARY KEY,
    meme_id CHAR(36),
    etiqueta TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
    confianza FLOAT,
    FOREIGN KEY (meme_id) REFERENCES memes(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE INDEX idx_meme_id ON etiquetas (meme_id);
