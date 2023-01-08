CREATE or REPLACE VIEW demanda_precio_producto as
SELECT *, 
(SELECT orp.valor from optimizacion_restriccionproducto orp WHERE producto_id = op.id and orp.nombre = 'RBN') as RBNmin,
(SELECT orp.valor from optimizacion_restriccionproducto orp WHERE producto_id = op.id and orp.nombre = 'Max RVP Index') as IMPVRmax,
(SELECT orp.valor from optimizacion_restriccionproducto orp WHERE producto_id = op.id and orp.nombre = 'Max Sulfur (ppm)') as Azufemax,
(SELECT orp.valor from optimizacion_restriccionproducto orp WHERE producto_id = op.id and orp.nombre = 'Min SPG') as Densidadmin

FROM optimizacion_productofinal op 
order by nombre ASC   