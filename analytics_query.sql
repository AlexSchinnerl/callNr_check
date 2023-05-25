SELECT
   CAST(SUBSTRING("Physical Items"."Holding Details"."Normalized Call Number" FROM 8 FOR 6) AS INT) s_3,
FROM "Physical Items"
WHERE
(("Library Unit"."Library Code" = 'KHB') AND ("Location"."Location Code" = 'MAG1') AND (evaluate('REGEXP_INSTR(%1, ''^[0-9]{1,6}-[A-Z]{1}'')',"Holding Details"."Permanent Call Number") = '1'))
ORDER BY 4 ASC NULLS FIRST
FETCH FIRST 10000001 ROWS ONLY
