SELECT TA.NOMBRE_PAIS, TA.NOMBRE_CIUDAD, TA.CANTIDAD AS CANTIDAD_POR_CIUDAD, TB.CANTIDAD AS CANTIDAD_POR_PAIS, 
    (TA.CANTIDAD::FLOAT * 100)/TB.CANTIDAD::FLOAT AS PORCENTAJE
FROM(
    SELECT PC.PAIS AS NOMBRE_PAIS , PC.CIUDAD AS NOMBRE_CIUDAD,  PC.CANTIDAD_CLIENTES AS  CANTIDAD
    FROM(
        SELECT CIUDAD.NOMBRE_CIUDAD AS CIUDAD,
        PAIS.NOMBRE_PAIS AS PAIS, COUNT(CLIENTE.NOMBRE_CLIENTE) AS CANTIDAD_CLIENTES
        FROM PAIS, CIUDAD, CLIENTE
        WHERE 
            PAIS.CODIGO_PAIS = CIUDAD.CODIGO_PAIS
            AND CIUDAD.CODIGO_CIUDAD = CLIENTE.CODIGO_CIUDAD
        GROUP BY
            CIUDAD.NOMBRE_CIUDAD,
            PAIS.NOMBRE_PAIS
    ) PC
    GROUP BY 
        PAIS, CIUDAD, CANTIDAD_CLIENTES
) TA,
( 
   SELECT PP.PAIS AS NOMBRE_PAIS, PP.CANTIDAD_CLIENTES AS CANTIDAD
    FROM(
        SELECT PAIS.NOMBRE_PAIS AS PAIS, COUNT(CLIENTE.NOMBRE_CLIENTE) AS CANTIDAD_CLIENTES
        FROM PAIS, CIUDAD, CLIENTE
        WHERE 
            PAIS.CODIGO_PAIS = CIUDAD.CODIGO_PAIS
            AND CIUDAD.CODIGO_CIUDAD = CLIENTE.CODIGO_CIUDAD
        GROUP BY
            PAIS.NOMBRE_PAIS
        
    ) PP
    GROUP BY 
        PP.PAIS, PP.CANTIDAD_CLIENTES 
) TB
WHERE
    TA.NOMBRE_PAIS = TB.NOMBRE_PAIS
ORDER BY    
    TA.NOMBRE_PAIS ASC
;