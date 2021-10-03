SELECT TB.PAIS, TB.CIUDAD, TB.NUMERO_RENTAS
FROM(
    SELECT TA.PAIS, TA.CIUDAD, MAX(RENTAS) AS NUMERO_RENTAS
    FROM(
        SELECT CATEGORIA.NOMBRE_CATEGORIA AS CATEGORIA, PAIS.NOMBRE_PAIS AS PAIS, CIUDAD.NOMBRE_CIUDAD
        AS CIUDAD, COUNT(*) AS RENTAS
        FROM PAIS, CIUDAD, CLIENTE, RENTA, PELICULA, CATEGORIA_PELICULA, CATEGORIA
        WHERE
            PAIS.CODIGO_PAIS = CIUDAD.CODIGO_PAIS
            AND CIUDAD.CODIGO_CIUDAD = CLIENTE.CODIGO_CIUDAD
            AND RENTA.CODIGO_CLIENTE = CLIENTE.CODIGO_CLIENTE
            AND RENTA.CODIGO_PELICULA = PELICULA.CODIGO_PELICULA
            AND PELICULA.CODIGO_PELICULA = CATEGORIA_PELICULA.CODIGO_PELICULA
            AND CATEGORIA.CODIGO_CATEGORIA = CATEGORIA_PELICULA.CODIGO_CATEGORIA
        GROUP BY
            CATEGORIA.NOMBRE_CATEGORIA, PAIS.NOMBRE_PAIS, CIUDAD.NOMBRE_CIUDAD
    ) TA
    GROUP BY 
        PAIS, CIUDAD
    ORDER BY
        PAIS, CIUDAD
) TB,
(
    SELECT CATEGORIA.NOMBRE_CATEGORIA AS CATEGORIA, PAIS.NOMBRE_PAIS AS PAIS, 
        CIUDAD.NOMBRE_CIUDAD AS CIUDAD, COUNT(*) RENTAS
    FROM PAIS, CIUDAD, CLIENTE, RENTA, PELICULA, CATEGORIA_PELICULA, CATEGORIA
    WHERE
        PAIS.CODIGO_PAIS = CIUDAD.CODIGO_PAIS
        AND CIUDAD.CODIGO_CIUDAD = CLIENTE.CODIGO_CIUDAD
        AND RENTA.CODIGO_CLIENTE = CLIENTE.CODIGO_CLIENTE
        AND RENTA.CODIGO_PELICULA = PELICULA.CODIGO_PELICULA
        AND PELICULA.CODIGO_PELICULA = CATEGORIA_PELICULA.CODIGO_PELICULA
        AND CATEGORIA.CODIGO_CATEGORIA = CATEGORIA_PELICULA.CODIGO_CATEGORIA
    GROUP BY
        CATEGORIA.NOMBRE_CATEGORIA, PAIS.NOMBRE_PAIS, CIUDAD.NOMBRE_CIUDAD
) TC
WHERE
    CATEGORIA = 'Horror'
    AND TB.PAIS = TC.PAIS
    AND TB.CIUDAD = TC.CIUDAD
    AND TB.NUMERO_RENTAS = TC.RENTAS  
;